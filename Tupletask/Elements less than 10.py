#Count elements less than 10
My_Tuple=(1,2,3,5,66,7,8,45,9,67)
count=0
for i in My_Tuple:
    if(i<10):
        count+=1
print(count)