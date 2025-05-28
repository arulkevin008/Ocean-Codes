#Sqaured Tuple
Tuplenum = (2, 4, 5, 6, 7)
y=[]
for i in Tuplenum:
    y.append(i ** i)
square_Tuple = tuple(y)
print(square_Tuple)