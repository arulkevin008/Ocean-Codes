#Unique vowels in a string
str1=input("Enter a string:")
str1_Set=set(str1)
vowels={"a","e","i","o","u"}
unique_vowels=str1_Set & vowels
print(unique_vowels)
print("No of unique vowels:",len(unique_vowels))