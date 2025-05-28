#Check the range
start_range=int(input("Enter the starting range:"))
end_range=int(input("Enter the ending range:"))
def number_range(num):
    if(start_range<num<end_range):
        print("It is in the given range")
    else:
        print("It is not in the given range")
number_range(int(input("Enter the number:")))
    