#Salary
def salary():
    try:
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
    except:
        print("Error")
salary()