#Minimum Salary
a=int(input("Enter the salary of person A:"))
b=int(input("Enter the salary of person B:"))
c=int(input("Enter the salary of person C:"))
def minimum_salary(a,b,c):
    if(a<b and a<c):
        print("Employee A has the minimum salary")
    elif(b<a and b<c):
        print("Employee B has the minimum salary")
    elif(c<b and c<a):
        print("Employee C has the minimum salary")
    else:
        print("Salaries of the three employees are same")
minimum_salary(a,b,c)