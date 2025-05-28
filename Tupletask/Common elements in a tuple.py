#Print common elements in two Tuples
Tuple_one=(1,2,4,5,7,8,9)
Tuple_two=(2,4,6,7,8,5,3)
y=[]
for i in Tuple_one:
    for j in Tuple_two:
        if(i==j):
            y.append(i)
Common_num=tuple(y)
print(Common_num)