#Reverse of a number
def reverse():
    num=int(input("Enter the num:"))
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    print("Reverse of the number:",rev)
reverse()