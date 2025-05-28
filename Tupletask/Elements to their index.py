#Count elements to their index
My_Tuple=(0,1,2,3,4,5,6,8,9)
count = 0
i = 0
while i < len(My_Tuple):
    if My_Tuple[i] == i:
        count += 1
    i += 1
print("Count of elements equal to their index:", count)