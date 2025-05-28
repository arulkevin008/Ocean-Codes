#Remove elements less than 10
Tuple=[1,2,5,7,9,12,54,67]
y=list(Tuple)
for i in Tuple[:]:
    if(i<10):
        y.remove(i)
Looped_tuple=tuple(y)
print(Looped_tuple)