def day_week():
    try:
        day=int(input("Enter the day of the week:"))
        if (day==1):
            print("Sunday")
        elif (day==2):
            print("Monday")
        elif (day==3):
            print("Tuesday")
        elif (day==4):
            print("Wednesday")
        elif (day==5):
            print("Thursday")
        elif (day==6):
            print("Friday")
        elif (day==7):
            print("Saturday")
        else:
            print("There is no day!!")
    except:
        print("Error")
day_week()