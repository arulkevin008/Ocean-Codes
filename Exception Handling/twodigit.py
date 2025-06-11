def two_digit():
    try:
        n=int(input("Enter the no:"))
        if(9<n<100):
            print(n,"is two digit")
        else:
            print(n,"is not two digit")
    except:
        print("Error")
two_digit()