import math
import matplotlib.pyplot as plt
import numpy as np
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

def customerIsAvailable(ui): 
    x = -12 * math.log(1-ui)
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
    w = 0
    calls = 0
    iter = 0
    while calls < 4:
        calls += 1
        iter += 1
        w += TIME_TO_PICK_UP_PHONE
        callProbability = generateNthRandNum(i + iter) # (0, 1)
        # print(i + iter)
        if callProbability <= 0.2:
            w += TIME_TO_GET_BUSY_SIGNAL
        elif callProbability <= 0.5 and callProbability > 0.2:
            w += TIME_TO_HEAR_5_RINGS

        else: # callProbability (0.5, 1.0)
            # customer is AVAILABLE
            timeToAnswer = customerIsAvailable(u_list[i+iter+2000])
            if timeToAnswer >= 25:
                w += TIME_TO_HEAR_5_RINGS
            else:
                w += timeToAnswer
                break
        w += TIME_TO_END_CALL

    return w

w_list = []
f = open("out.txt", "a")
for w in range(1, 2001, 4):
    val = callCustomer(w)
    f.write(str(val) + "\n")
    w_list.append(val)
    if val > 128:
        print("OH NO SOMETHING WENT HORRIBLY WRONG")
f.close()
print(w_list)


lessThan15 = 0
lessThan20 = 0
lessThan30 = 0
lessThan128 = 0
moreThan40 = 0
moreThan60 = 0
moreThan80 = 0
moreThan120 = 0
for num in w_list:
    if num <= 6:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA WHY")
    if num <= 15:
        lessThan15 += 1
    if num <= 20:
        lessThan20 += 1
    if num <= 30:
        lessThan30 += 1
    if num <= 128:
        lessThan128 += 1
    if num > 40:
        moreThan40 += 1
    if num > 60:
        moreThan60 += 1
    if num > 80:
        moreThan80 += 1
    if num > 120:
        moreThan120 += 1
        print("big: " + str(num))

ratio =  lessThan15 / len(w_list) 
print("prob less than 15: " + str(ratio))

ratio =  lessThan20 / len(w_list) 
print("prob less than 20: " + str(ratio))

ratio =  lessThan30 / len(w_list) 
print("prob less than 30: " + str(ratio))

ratio =  lessThan128 / len(w_list) 
print("prob less than 128: " + str(ratio))

ratio =  moreThan40 / len(w_list) 
print("prob more than 40: " + str(ratio))

ratio =  moreThan60 / len(w_list) 
print("prob more than 60: " + str(ratio))

ratio =  moreThan80 / len(w_list) 
print("prob more than 80: " + str(ratio))

ratio =  moreThan120 / len(w_list) 
print("prob more than 120: " + str(ratio))
w_list = sorted(w_list)
#calc of mean, q1, median, and q3
meanOfW = np.mean(w_list)

quartiles = np.percentile(w_list, [25, 50, 75])
q1, median, q3 = quartiles


lessThan15 = np.sum(np.array(w_list) <= 15) / len(w_list)
lessThan20 = np.sum(np.array(w_list) <= 20) / len(w_list)
lessThan30 = np.sum(np.array(w_list) <= 30) / len(w_list)
moreThan40 = np.sum(np.array(w_list) > 40) / len(w_list)

w5, w6, w7 = 75, 100, 125
greaterThanW5 = np.sum(np.array(w_list) > w5) / len(w_list)
greaterThanW6 = np.sum(np.array(w_list) > w6) / len(w_list)
greaterThanW7 = np.sum(np.array(w_list) > w7) / len(w_list)

print(f"MeanOfW: {meanOfW}")
print(f"Q1: {q1}")
print(f"Median: {median}")
print(f"Q3: {q3}")
print(f"P[W] <= 15: {lessThan15}")
print(f"P[W] <= 20: {lessThan20}")
print(f"P[W] <= 30: {lessThan30}")
print(f"P[W] > 40: {moreThan40}")
print(f"P[W] > w5 (75): {greaterThanW5}")
print(f"P[W] > w6 (100): {greaterThanW6}")
print(f"P[W] > w7 (125): {greaterThanW7}")

vals = set(w_list)
freq = np.arange(1, len(vals)+1)
for n in sorted(list(set(w_list))):
    if n > 120:
        print(n)
# plt.bar(list(vals), freq, width=0.1)
plt.xlim(5, 129)
plt.bar(sorted(list(set(w_list))), np.arange(1, len(set(w_list))+1), width=0.5)



plt.show()
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