#Living time
import datetime
x=datetime.datetime.now()
y=x.year
d=x.strftime("%d")
m=x.strftime("%m")
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day:"))
if(year>y):
    print("Year Invalid")
    exit()
elif(0<=day>31):
    print("Date Invalid")
    exit()
elif(0<=month>12):
    print("Month Invalid")
    exit()
calculated_year=y-year
d=int(d)
calculated_day=d-day
calculated_day=abs(calculated_day)
m=int(m)
calculated_month=m-month
calculated_month=abs(calculated_month)
print("You lived ",calculated_year,"years",calculated_month,"month",calculated_day,"days!!")