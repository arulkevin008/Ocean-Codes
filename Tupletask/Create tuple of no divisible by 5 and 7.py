#Create Tuple of numbers divisible by 5 and 7
Tuple=()
y=list(Tuple)
for i in range(1,101):
    if(i%5==0):
        y.append(i)
    if(i%7==0):
        y.append(i)
Tuple=tuple(y)
print(Tuple)