#Multiply all numbers in a list
from functools import reduce
def Multiply(x,y):
    return x*y
num=[2,4,5,76,84]
result=reduce(Multiply,num)
print("Multiply =",result)