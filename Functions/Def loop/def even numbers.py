#Print even numbers from 1 to 100
def print_even():
    print("Even numbers")
    for i in range(1,101):
        if(i%2==0):
            print(i)
print_even()