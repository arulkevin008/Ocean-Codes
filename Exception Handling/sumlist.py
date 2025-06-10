def sum_list(lst):
    try:
        return sum(lst)
    except TypeError:
        return "List contains non-numeric data"

print(sum_list([1, 2, 3])) 
print(sum_list([1, 'a', 3]))  