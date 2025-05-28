#Sum numbers in a list using reduce
from functools import reduce
def Sum(x,y):
    return x+y
num=[2,4,5,76,84]
result=reduce(Sum,num)
print("Sum =",result)
