#Valid triangle
def valid_tri():
    try:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        c=int(input("Enter the value of c:"))
        d=a+b+c
        if (0<d<=180):
            print("It is a valid triangle!")
        else:
            print("It is an invalid trinagle!")
    except:
        print ("Error")
valid_tri()