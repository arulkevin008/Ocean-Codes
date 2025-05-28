#Even numbers from a list using filter
List=[1,3,4,5,67]
def EvenList(x):
    return True if x%2==0 else False
even_num=filter(EvenList,List)
print("Even numbers:")
for x in even_num:
    print(x,end=" ")