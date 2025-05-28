# 1.Leap Year
year=int(input("Enter the year:"))
if (year%4==0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")

# 2.Valid Triangle
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=a+b+c
if (0<d<=180):
    print("It is a valid triangle!")
else:
    print("It is an invalid trinagle!")

# 3.Vote Eligibility
age=int(input("Enter the age:"))
if (age>=18):
    print("You are Eligible to Vote")
else:
    print("You are not Eligible to Vote")

# 4.Day of the week
day=int(input("Enter the day of the week:"))
if (day==1):
    print("Sunday")
elif (day==2):
    print("Monday")
elif (day==3):
    print("Tuesday")
elif (day==4):
    print("Wednesday")
elif (day==5):
    print("Thursday")
elif (day==6):
    print("Friday")
elif (day==7):
    print("Saturday")
else:
    print("There is no day!!")

# 5.Operator
a=int(input("Enter a no:"))
b=int(input("Enter a no:"))
c=input("Enter the operation:")
if(c in ("+")):
    print("Addition:",a+b)
elif(c in ("-")):
    print("Subtraction:",a-b)
elif(c in ("*")):
    print("Mutiplication:",a*b)
elif(c in ("/")):
    print("Division:",a/b)
elif(c in ("%")):
    print("Modulus:",a%b)
else:
    print("Invalid Operation!")

# 6.Divisible by 5 or 3
n=int(input("Enter the no:"))
if(n%5==0 and n%3==0):
    print("The no is divisible by 5 and 3")
elif(n%5==0):
    print("The no is divisible by 5")
elif(n%3==0):
    print("The no is divisible by 3")
else:
    print("The no is not divisible by 5 and 3")

# 7.Vowel or Consonant
c=input("Enter a character:")
if c in("a","e","i","o","u"):
    print("Vowel")
else:
    print("Consonant")

# 8.Check the digit
num1=int(input("Enter the no:"))
if (num1<100 and num1%10==0):
    print("Ones")
elif (100<num1<1000 and num1%100==0):
    print("Twos")
else:
    print("Invalid input")
