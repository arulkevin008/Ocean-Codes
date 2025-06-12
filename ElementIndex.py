def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

print(get_element([1, 2, 3], 1))  
print(get_element([1, 2, 3], 5))  
