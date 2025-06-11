#Grade
def grade():
    try:
        per=int(input("Enter Your Percentage:"))
        if (90<per<=100):
            print("S Grade!!")
        elif (80<per<=90):
            print("A Grade!!")
        elif (70<per<=80):
            print("B Grade!!")
        elif (60<per<=70):
            print("C Grade!!")
        elif (50<per<=60):
            print("D Grade!!")
        elif (40<per<=50):
            print("E Grade!!")
        else:
            print("F Grade!!")
    except:
            print("Error")
grade()