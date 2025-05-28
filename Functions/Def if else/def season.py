#Season
month=input("Enter the season:")
month=month.capitalize()
def season():
    if month in("March" , "April"):
        print(month,"Spring Season!")
    elif month in("May" , "June" , "July"):
        print(month,"Summer Season!")
    elif month in( "August","September" , "October" , 'November'):
        print(month,"Autumn Season!")
    elif month in('December' , 'January','February'):
        print(month,"Winter Season!")
    else:
        print(month,"Enter a valid month!!")
season()