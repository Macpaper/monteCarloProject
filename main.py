import random
import math
# random.seed(random.randint(0,10000000))

# for i in range(1000):
#     print(random.uniform(0, 1))
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

# generate a realization of x_i
# x_i = minimum x for which F(x) >= u_i
# you can find this value by sequentially searching 
# over x = 1...k until F(x) >= u_i for the first time


print(generateNthRandNum(1))
print(generateNthRandNum(2))
print(generateNthRandNum(3))
u51 = generateNthRandNum(51)
u52 = generateNthRandNum(52)
u53 = generateNthRandNum(53)
print(u51)
print(u52)
print(u53)
TIME_TO_PICK_UP_PHONE = 6
TIME_TO_GET_BUSY_SIGNAL = 3
TIME_TO_END_CALL = 1
TIME_TO_HEAR_5_RINGS = 25
mean = 12
lam = 1/mean
def sumX():
    sum = 0
    for i in range(1, 6):
        sum += generateNthRandNum(i)
    return sum
         
min(sumX(), generateNthRandNum(5))
def callCustomer():
    # W = random variable. # of seconds spent calling customer
    w = TIME_TO_PICK_UP_PHONE
    lol = random.randint(0, 10000)
    for i in range(lol, lol+4):
        callProbability = generateNthRandNum(i)
        if callProbability <= 0.2:
            w += TIME_TO_GET_BUSY_SIGNAL
            break
        elif callProbability <= 0.5:
            w += TIME_TO_HEAR_5_RINGS
        else:
            # customer is AVAILABLE
            timeToAnswer = customerIsAvailable(i)
            if timeToAnswer >= 25:
                w += TIME_TO_HEAR_5_RINGS
            else:
                w += timeToAnswer
                break
    w += TIME_TO_END_CALL

def exponentialCDFatX(lam, x):
    cdfAtX = 1 - math.e**(-lam * x)
    return cdfAtX

def customerIsAvailable(i): 
    x = -math.log(1-generateNthRandNum(i)) * 12
    math.log(127891)
    math.log(15)
    math.log(4)
    math.log(98)
    print(x)
    return x
# for i in range(10):
    # callCustomer()