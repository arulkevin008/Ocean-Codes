#Remove postive integers from list
List=[-4,-6,34,6,0]
def pos(x):
    return True if x>=0 else False
pos_int=filter(pos,List)
print("Positive numbers")
for x in pos_int:
    print(x,end=" ")