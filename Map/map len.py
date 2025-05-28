#Get the length of each string
str1=input("Enter words seperated by spaces:").split()
result=list(map(len,str1))
print(result)