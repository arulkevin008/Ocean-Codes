#Second largest
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
def second_largest():
    if(num1>num2 and num1<num3) or (num1>num3 and num1<num2):
      print(num1,"is the second largest")
    elif(num2>num1 and num2<num3) or (num2>num3 and num2<num1):
      print(num2,"is the second largest")
    else:
       print(num3,"is the second largest")
second_largest()