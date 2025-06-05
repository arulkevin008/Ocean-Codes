#DateTime
import datetime
x=datetime.datetime.now()
print(x)
print("Day short form:",x.strftime("%a"))
print("Day full form:",x.strftime("%A"))
print("Weekday:",x.strftime("%w"))
print("Day of month:",x.strftime("%W"))
#y=x.year
#year=int(input("Enter your year:"))
#print("Age:",y-year)