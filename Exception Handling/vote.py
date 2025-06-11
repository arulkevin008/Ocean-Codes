def eligibility():
    try:
        age=int(input("Enter the age:"))
        if (age>=18):
            print("You are Eligible to Vote")
        else:
            print("You are not Eligible to Vote")
    except:
        print("Error")
eligibility()