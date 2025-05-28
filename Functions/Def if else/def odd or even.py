#Odd or Even
def odd_or_even(num):
    if(num%2==0):
        print(num,"is an even number.")
    else:
        print(num,"is an odd number.")
odd_or_even(int(input("Enter the number:")))