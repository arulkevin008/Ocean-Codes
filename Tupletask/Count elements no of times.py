#Count number of times
MyTuple=(2,3,4,5,2,5,7,9,4)
num=int(input("Enter the number to count:"))
num_count=0
for i in MyTuple:
    if(num==i):
            num_count+=1
print("The no of times are:",num_count)
