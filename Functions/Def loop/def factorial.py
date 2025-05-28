#Factorial
def factorial():
    fact=1
    num=int(input("Enter the num:"))
    for i in range(1,num+1):
        fact*=i
    print(fact)
factorial()