#1.No from 1 to 15.
##for i in range(1,16):
##    print(i)

#2.No from 6 to 29.
##for i in range(6,30):
##    if i%2==1:
##        print(i)

#3.Even No from 20 to 40.
##for i in range(20,41):
##    if i%2==0:
##        print(i)

#4.Divisible by 3,5.
for i in range(1,16):
    if(i%3==0):
        print(i,"Divisible by 3")
        if(i%5==0):
            print(i,"Divisible by 5")
            if(i%3==0 and i%5==0):
                print(i,"Divisible by 3 and 5")

#5.Elements of a list.
##list=[0,5,10,15,20]
##for i in list:
##    print(i)

#6.Sum of Elements of a list.
##list=[0,5,10,15,20]
##Sum=0
##for i in list:
##    Sum+=i
##    print(Sum)

#7.Sum of 1 to 100.
##Sum=0
##for i in range(1,100):
##    Sum+=i
##print(Sum)



#8.Factorial of a number.
##n=int(input("Enter a number:"))
##fact=1
##for i in range(fact,n+1):
##    fact*=i
##print(fact)

#9.Maximum element of a list.
##MyList = [0,5,10,15,20]
##s = MyList[0]
##for i in MyList:
##    if(i>s):
##        s=i
##print("The maximum value is:",s)

#10.Fibonacci series.
##n=int(input("Enter the no of times series to be executed:"))
##a=0
##b=1
##print(a)
##print(b)
##for i in range(n):
##    c=a+b
##    print(c)
##    a=b
##    b=c

