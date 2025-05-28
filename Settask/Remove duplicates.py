#Remove duplicates
my_set={2,2,4,6,5}
dups = {}
for i in range(len(my_set)):
    for j in range(i+1, len(my_set)):
        if my_set[i] == my_set[j] and my_set[i] not in dups:
            dups.update(my_set[i])
print(dups)