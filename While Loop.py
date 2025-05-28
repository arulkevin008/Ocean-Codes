#While Loop
#1.Multiplication Table.
print("1.Multiplication Table\n")
n=int(input("Enter a table:"))
i=0
while(i<11):
    print(i,"*",n,"=",i*n)
    i+=1

#2.No from 1 to 10.
print("\n2.No from 1 to 10\n")
i=1
while(i<11):
    print(i)
    i+=1

#3.Sum of n natural numbers.
print("\n3.Sum of natural number\n")
n=int(input("Enter a natural number:"))
i=0
total=0
while(i<=n):
    total+=i
    i+=1
print(total)

#4.Factorial of a Number.
print("\n4.Factorial of a Number\n")
n=int(input("Enter the factorial of a number:"))
fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print(fact)

#5.Even no from 1 to 100.
print("\n5.Even no from 1 to 100\n")
i=1
while(i<101):
    i+=1
    if(i%2==0):
        print(i)

#6.Odd no from 1 to 100.
print("\n6.Odd no from 1 to 100\n")
i=0
while(i<100):
    i+=1
    if(i%2==1):
        print(i)

#7.Palindrome.
print("\n7.Palindrome number\n")
num=int(input("Enter a palindrome number:"))
n=num
rev=0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if(n==rev):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#8.Armstrong number.
print("\n8.Armstrong number\n")
n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
Sum = 0
while temp > 0:
    digit = temp % 10
    Sum += digit ** digits
    temp //= 10
if n == Sum:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")

#9.Reverse of a number.
print("\n9.Reverse of a number\n")
num=int(input("Enter a no:"))
n=num
rev=0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

#10.Prime no from 1 to 100.
print("\n10.Prime no from 1 to 100\n")
n=2
while(n<= 100):
    prime= True
    i=2
    while(i<=n//2):
        if(n%i==0):
            prime=False
            break
        i += 1
    if prime:
        print(n)
    n+= 1

