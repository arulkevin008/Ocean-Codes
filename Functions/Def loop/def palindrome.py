#Palindrome
def palindrome():
    num=int(input("Enter the num:"))
    n=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    if(rev==n):
        print(rev,"The given no is palindrome")
    else:
        print(rev,"The given no is not palindrome")
palindrome()