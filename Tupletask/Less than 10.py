#Less than 10
Tuple=(2,4,5,23,56,67,7)
x=[]
for i in Tuple:
    if(i<10):
        x.append(i)
Tuple_10=tuple(x)
print(Tuple_10)