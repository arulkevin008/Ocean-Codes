#Avg of a Tuple
Tuple=(2,4,6,78)
Tuple_avg=()
Sum=0
for i in Tuple:
    Sum+=i
Tuple_avg=(Sum/len(Tuple))
print(Tuple_avg)