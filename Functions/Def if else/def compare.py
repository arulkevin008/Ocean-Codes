#Largest Number
a=int(input("Enter a:"))
b=int(input("Enter b:"))
def largest_number(a,b):
    if(a>b):
        print(a,"is largest number")
    elif(a<b):
        print(b,"is largest number")
    elif(a==b):
        print(a,"and",b,"are equal")
largest_number(a,b)