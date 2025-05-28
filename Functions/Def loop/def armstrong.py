#Armstrong number
def armstrong_number():
    n=int(input("Enter the no:"))
    temp=n
    digits=len(str(n))
    Sum=0
    while temp>0:
        digit=temp%10
        Sum=Sum+digit**digits
        temp//=10
    if(Sum==n):
        print(Sum,"is an armstrong number")
    else:
        print(Sum,"is not an armstrong number")
armstrong_number()
