#Remove all zeroes
list_numbers=[0,2,3,5,0,5,6]
for i in list_numbers:
    if(i==0):
        list_numbers.remove(i)
print(list_numbers)