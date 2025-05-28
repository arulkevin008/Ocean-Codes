#Second Largest Number
nums=[8, 3, 12, 5, 12, 7]
count=0
largest=nums[0]
second_largest=nums[0]
index=0
for num in nums:
    if (index!=0): 
        if(num>largest):
            second_largest=largest
            largest=num
        elif num!=largest and (second_largest==largest or num>second_largest):
            second_largest = num
    index = index + 1
if second_largest==largest:
    second_largest=None
print("Second largest:",second_largest)