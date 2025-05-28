#Grade Percentage
def grade_percentage(per):
    if (90<per<=100):
        print(per,"S Grade!!")
    elif (80<per<=90):
        print(per,"A Grade!!")
    elif (70<per<=80):
        print(per,"B Grade!!")
    elif (60<per<=70):
        print(per,"C Grade!!")
    elif (50<per<=60):
        print(per,"D Grade!!")
    elif (40<per<=50):
        print(per,"E Grade!!")
    else:
        print(per,"F Grade!!")
grade_percentage(int(input("Enter the number:")))
