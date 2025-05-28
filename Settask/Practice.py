#Common element in two list
List1=[23,45,76,89,23]
List2=[45,67,78,3,23]
Common_List=[]
for i in List1:
    if(i in List2):
        Common_List.append(i)
Common_List=set(Common_List)
print("\t\t\tCommon Element\n")
print(list(Common_List))

#Coin Toss
import random
options=("Heads","Tails")
toss=random.choice(options)
print("\t\t\tCoin Toss\n")
print(toss)