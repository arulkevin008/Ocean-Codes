#Eligibility to vote
def vote_eligibility(age):
    if(0<age<18):
        print("You are not eligible to vote!")
    elif(age>=18):
        print("You are eligible to vote")
vote_eligibility(age=int(input("Enter your age:")))
