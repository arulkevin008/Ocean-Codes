#Check the number exist in the set
my_set={2,3,5,6,67,4}
num=int(input("Enter the element to check:"))
if(num in my_set):
    print(num,"exists!")
else:
    print(num,"does not exists!")