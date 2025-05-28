#Concatenate all strings in a list using reduce
from functools import reduce
def concatenate(x,y):
    return x+" "+y
str1=["Welcome","to","Python","Programming"]
str_concatenate=reduce(concatenate,str1)
print(str_concatenate)