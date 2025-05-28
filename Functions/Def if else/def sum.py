#Check sum is even or odd
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=a+b
def sum_even_or_odd():
    if(c%2==0):
        print(c,"The sum is an even number")
    else:
        print(c,"The sum is an odd number")
sum_even_or_odd()