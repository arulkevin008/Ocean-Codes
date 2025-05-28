MyTuple=(-1,-4,-6,2,5,8,0,9,0,-7)
positive_num=[]
negative_num=[]
zero=[]
for i in MyTuple:
    if(i<0):
        negative_num.append(i)
    elif(i>0):
        positive_num.append(i)
    elif(i==0):
        zero.append(i)
positive_num=tuple(positive_num)
negative_num=tuple(negative_num)
zero=tuple(zero)
print("Positive numbers:",positive_num)
print("Negative numbers:",negative_num)
print("Zero",zero)