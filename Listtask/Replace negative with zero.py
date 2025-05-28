#Replace negative with zero
num=[-2,2,4,-4,1]
for i in range(len(num)):
    if num[i]<0:
        num[i]=0
print(num)