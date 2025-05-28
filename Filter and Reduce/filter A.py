#Keep names that start with "A"
Name_List=["Arul","Bhuvan","Naren","Mani","Ravi","Sanjay"]
def str_a(x):
    return True if x[0]=="A"or x[0]=="a" else False
str_name=filter(str_a,Name_List)
print("Str starts with \"A\":")
for x in str_name:
    print(x,end=" ")
