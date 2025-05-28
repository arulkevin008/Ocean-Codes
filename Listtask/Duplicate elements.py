#Duplicate elements
List=[2,2,4,6,5]
dups = []
for i in range(len(List)):
    for j in range(i+1, len(List)):
        if List[i] == List[j] and List[i] not in dups:
            dups.append(List[i])
print(dups)