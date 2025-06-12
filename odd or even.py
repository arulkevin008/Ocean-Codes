def odd_even():
    try:
        n=int(input("Enter the no:"))
        if(n%2==0):
            print(n,"is even")
        else:
            print(n,"is odd")
    except:
        print("Error")
odd_even()