#Average of a List
List=[2,4,6,78]
list_avg=[]
for i in List:
    i+=i
list_avg=[i/len(List)]
print(list_avg)