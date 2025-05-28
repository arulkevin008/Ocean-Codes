#Replace even numbers with -1
My_list=[2,3,4,5,6,7,8,9]
for i in range(len(My_list)):
    if My_list[i]%2==0:
        My_list[i]=0
print(My_list)