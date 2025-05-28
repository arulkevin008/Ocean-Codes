#Print odd numbers from 1 to 100
def print_odd():
    print("Odd numbers")
    for i in range(1,101):
        if(i%2==1):
            print(i)
print_odd()