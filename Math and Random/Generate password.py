#Password Generator
import random
options=[0,1,2,3,4,5,6,7,8,9]
length=6
print("Password:")
while length>0:
    i=random.choice(options)
    print(i,end="")
    length-=1