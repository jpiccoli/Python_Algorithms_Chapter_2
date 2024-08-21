import math
import pandas as pd

######################################################
def RPM():
    n1 = 89
    n2 = 18

    halving =[n1]

    while(min(halving) > 1):
        halving.append(math.floor(min(halving)/2))

    doubling = [n2]

    while(len(doubling) < len(halving)):
        doubling.append(max(doubling) * 2)

    half_double = pd.DataFrame(zip(halving, doubling))

    half_double = half_double.loc[half_double[0] %2 == 1, :]

    answer = sum(half_double.loc[:,1])

    print('Answer = ' + str(answer))

######################################################
def gcd(x, y):
    larger = max(x,y)
    smaller = min(x, y)

    remainder = larger % smaller

    if(remainder == 0):
        print('GCD = ' + str(smaller))
        return smaller

    if(remainder != 0):
        return(gcd(smaller, remainder))

######################################################
RPM()
gcd(32, 12)