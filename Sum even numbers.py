#Sum even numbers
My_List=[1,2,3,5,6,7,8,0]
Even_sum=0
for i in My_List:
    if(i%2==0):
        Even_sum+=i
print(Even_sum)