#Sides of a triangle
a=int(input("Enter the value of side a:"))
b=int(input("Enter the value of side b:"))
c=int(input("Enter the value of side c:"))
def sides_of_a_triangle(a,b,c):
    if(a==b==c):
        print("It is an equilateral triangle!")
    elif(a==b or b==c or a==c):
        print("It is an isosceles triangle!")
    elif(a!=b!=c):
        print("It is a scalene triangle!")
sides_of_a_triangle(a,b,c)