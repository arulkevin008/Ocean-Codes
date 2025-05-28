#Create list of numbers divisible by 5 and 7
List=[]
for i in range(1,101):
    if(i%5==0):
        List.append(i)
    if(i%7==0):
        List.append(i)
print(List)