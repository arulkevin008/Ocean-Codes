#Print common elements in two lists
List_one=[1,2,4,5,7,8,9]
List_two=[2,4,6,7,8,5,3]
Common_list=[]
for i in List_one:
    for j in List_two:
        if(i==j):
            Common_list.append(i)
print(Common_list)


