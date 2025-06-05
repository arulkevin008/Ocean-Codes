#List addition
List=[[25,45,12],[45,34,12],[34,23,76],[67,45,23]]
Added_List=[]
Sum=0
for Data in List:
    Sum=0
    for i in Data:
        Sum+=i
    Added_List.append(Sum)
print(Added_List)