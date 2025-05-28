#Leap Year
def leap_year(year):
    if(year%4==0):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
leap_year(int(input("Enter the year:")))