#3. Grade Percentage
per=int(input("Enter Your Percentage:"))
if (90<per<=100):
    print("S Grade!!")
elif (80<per<=90):
    print("A Grade!!")
elif (70<per<=80):
    print("B Grade!!")
elif (60<per<=70):
    print("C Grade!!")
elif (50<per<=60):
    print("D Grade!!")
elif (40<per<=50):
    print("E Grade!!")
else:
    print("F Grade!!")

#4. Sides of the Triangle
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a==b==c):
    print("It is an Equilateral Trinagle.")
elif(a==b or b==c or a==c):
    print("It is an Isoceles Triangle.")
else:
    print("It is a Scalene Triangle.")


#5. Season of the Month
n=input("Enter the month:")
if n in("March" , "April" , "May"):
    print("Spring Season!")
elif n in("June" , "July" , "August"):
    print("Summer Season!")
elif n in("September" , "October" , 'November'):
    print("Autumn Season!")
elif n in('December' , 'January' , 'February'):
    print("Winter Season!")
else:
    print("Enter a valid month!!")

#7. Minimum Salary
a=int(input("Enter The Salary of employee A:"))
b=int(input("Enter The Salary of employee B:"))
c=int(input("Enter The Salary of employee C:"))
if(a<b and a<c):
    print("Employee A has the minimum salary")
elif(b<a and b<c):
    print("Employee B has the minimum salary")
elif(c<b and c<a):
    print("Employee C has the minimum salary")
else:
    print("Salaries of the three employees are same")

#8 Leap Year


