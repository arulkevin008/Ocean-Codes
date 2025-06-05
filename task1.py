#Age calculator
import datetime
x=datetime.datetime.now()
y=x.year
year=int(input("Enter your year:"))
if(year>y):
    print("Year Invalid")
    exit()
print("Age:",y-year)