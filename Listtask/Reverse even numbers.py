My_list = [2,3,4,5,6,7,8,9]
even_numbers = [num for num in My_list if num % 2 == 0]
even_numbers.reverse()
j = 0 
for i in range(len(My_list)):
    if My_list[i] % 2 == 0:
        My_list[i] = even_numbers[j]
        j += 1
print(My_list)