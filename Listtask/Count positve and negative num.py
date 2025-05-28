#Count +ve and -ve num
MyList=[-1,-4,-6,2,5,8]
positive=0
negative=0
for i in MyList:
    if(i<0):
        negative+=1
    elif(i>=0):
        positive+=1
print("Positive numbers:",positive)
print("Negative numbers:",negative)