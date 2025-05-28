#Remove elements less than 10
List=[1,2,5,7,9,12,54,67]
for i in List[:]:
    if(i<10):
        List.remove(i)
print(List)