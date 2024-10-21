import math

# Finding the inverse CDF of exponential random variable X with lambda = 1/12, E(X) = 12
# F(x) = u
# x = F^-1(u)
# u = 1 - e^(-1/12x)
# e^(-1/12x) = 1 - u
# -1/12x = ln(1-u)
# x = -ln(1-u)*12
# x_i = -ln(1-u_i) * 12

def generateNthRandNum(n):
    x = 1000 # 'seed'
    a = 24_693
    c = 3517
    K = 2**17
    u = 0
    for i in range(n):
        lastNum = x
        x = (lastNum * a + c) % K
        u = x / K
    return u

def customerIsAvailable(i): 
    x = -math.log(1-generateNthRandNum(i)) * 12
    return x

# Generate a list of random variables from (0, 1) using random number generator.
u_list = []
for i in range(1, 10002):
    u_list.append(generateNthRandNum(i))

# u1, u2, u3 and u51, u52, u53 are printed here
print(generateNthRandNum(1))    
print(generateNthRandNum(2))
print(generateNthRandNum(3))
print(generateNthRandNum(51))
print(generateNthRandNum(52))
print(generateNthRandNum(53))

# Fields for phone time
TIME_TO_PICK_UP_PHONE = 6
TIME_TO_GET_BUSY_SIGNAL = 3
TIME_TO_END_CALL = 1
TIME_TO_HEAR_5_RINGS = 25

mean = 12 # Expected time it takes for available customer to pick up phone is 12 seconds
lam = 1/mean 

# Generates a call for a single customer
def callCustomer(i):
    # w is number of seconds spent calling customer i
    w = TIME_TO_PICK_UP_PHONE
    timesCalled = 0
    iter = 0
    while timesCalled < 4:
        timesCalled += 1
        callProbability = generateNthRandNum(i + iter)
        if callProbability <= 0.2:
            w += TIME_TO_GET_BUSY_SIGNAL
        elif callProbability <= 0.5:
            w += TIME_TO_HEAR_5_RINGS
        else:
            # customer is AVAILABLE
            timeToAnswer = customerIsAvailable(i + iter)
            if timeToAnswer > 25:
                w += TIME_TO_HEAR_5_RINGS
            else:
                w += timeToAnswer
                break
        iter += 1
    w += TIME_TO_END_CALL
    return w

w_list = []
for w in range(1, 501):
    val = callCustomer(w)
    w_list.append(val)
    if val > 107:
        print("OH NO SOMETHING WENT HORRIBLY WRONG")
print(w_list)


# SOME NOTES:
# There are a lot of repeating values of W. Consider this:
# There is a probability that the customer is ALWAYS busy. This is 6 + 3*4 + 1 = 19
# There is a probability that the customer is ALWAYS unavailable. This is 6 + 25*4 + 1 = 107
# There is a probability that the customer is ALWAYS some combination of busy or unavailable. 
#   This is a set of whole numbers between 19 and 107 with a combination of 4(c) + 25(1-c) 
#   where c is the number of times called.
# Any other number is the time it takes the customer to answer before 25 seconds.
#   This number should always be less than 107. 
# Every single w should be less than or equal to 107 (verified above this btw)

# probably dont need this lol
# def exponentialCDFatX(lam, x):
#     cdfAtX = 1 - math.e**(-lam * x)
#     return cdfAtX