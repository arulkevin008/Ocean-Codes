#Guess the number
print("\t\t\tGuess the Number\t\t\t\n")
while True:
    import random
    number=int(input("Enter the no:"))
    random_number=random.randint(1,11)
    if(number==random_number):
        print(number,"is correct")
    elif(number!=random_number):
        print(number,"is wrong")