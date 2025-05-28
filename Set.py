###Convert List of words to Set
##List=["apple","banana","cherry","orange"]
##Set=set(List)
##print(Set)
##
##A={23,54,56,76}
##B={45,64,32,45}
##C=A.isdisjoint(B)
##print(C)

str1=input("Enter a string:")
unique_char=set(str1)
print(unique_char)
count=len(unique_char)
print("No of unique char:",count)
