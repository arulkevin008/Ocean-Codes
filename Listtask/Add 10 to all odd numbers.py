# Add 10 to odd numbers
List=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_List=[]
for i in List:
    if (i%2==1):
        new_List.append(i+10)
    else:
        new_List.append(i)
print(new_List)