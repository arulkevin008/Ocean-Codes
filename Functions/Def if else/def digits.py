#Check the digit of the number
def digit_numbers(num):
    if(0<num<10):
        print("It is 1 digit!")
    elif(9<num<100):
        print("It is 2 digit!")
    elif(99<num<1000):
        print("It is 3 digit!")
digit_numbers(int(input("Enter the number:")))