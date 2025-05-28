#Find maximum number
from functools import reduce
def Maximum(x,y):
    return x if x>y else y
num=[2,4,5,76,84]
result=reduce(Maximum,num)
print("Maximum num is",result)
        