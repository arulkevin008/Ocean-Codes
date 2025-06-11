#Season
def season():
    try:
        n=input("Enter the month:")
        if n in("March" , "April" , "May"):
            print("Spring Season!")
        elif n in("June" , "July" , "August"):
            print("Summer Season!")
        elif n in("September" , "October" , 'November'):
            print("Autumn Season!")
        elif n in('December' , 'January' , 'February'):
            print("Winter Season!")
        else:
            print("Enter a valid month!!")
    except:
        print("Error")
season()