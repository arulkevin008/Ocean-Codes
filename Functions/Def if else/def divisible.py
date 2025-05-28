#Divisible by 2 or 7
def divisible_2_or_7(num):
    if(num%2==0 and num%7==0):
        print("It is divisible by 2 and 7")
    elif(num%2==0):
        print("It is divisible by 2")
    elif(num%7==0):
        print("It is divisble by 7")
    else:
        print("It is not divisible by 2 and 7")
divisible_2_or_7(int(input("Enter the no:")))