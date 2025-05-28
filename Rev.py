##a=int(input("Enter a number:"))
##rev=0
##while a>0:
##    digit=a%10
##    rev=rev*10+digit
##    a//=10
##print("The reverse of the number:",rev)
    
##for i in range(1,51):
##       if(i%3==0 and i%5==0):
##            print(i,"Fizz Buzz")
##       elif(i%3==0):
##            print(i,"Fizz")
##       elif(i%5==0):
##            print(i, "Buzz")

rows=5
for i in range(1,rows+1):
    print("*"*i)

rows=5
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*i)
         
for i in range(1,5):
    if (i==1 or i==4):
        print("****")
    else:
        print("*  *")
