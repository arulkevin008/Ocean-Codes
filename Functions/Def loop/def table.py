#Multiplication table
def table():
    table=int(input("Enter the table:"))
    for i in range(1,11):
        print(i,"*",table,"=",i*table)
table()