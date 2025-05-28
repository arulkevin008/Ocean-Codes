#Len of string longer than 3
List=["App","Oneplus","Samsung","Re"]
def len_list(x):
    return True if len(x)>3 else False
length_str=filter(len_list,List)
for x in length_str:
    print(x,end=" ")
