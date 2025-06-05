#Age calculator
import datetime
x=datetime.datetime.now()
y=x.year
year=int(input("Enter your year:"))
print("Age:",y-year)

#Living time
y=x.year
day=x.strftime("%d")
month=x.strftime("%m")
