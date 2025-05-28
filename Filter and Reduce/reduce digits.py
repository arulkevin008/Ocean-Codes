#Create number from digits 
from functools import reduce
def digits(x,y):
    return x*10+y
num=[1,2,3,4,5]
num_digits=reduce(digits,num)
print(num_digits)