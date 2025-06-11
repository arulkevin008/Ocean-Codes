def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return 0
print(convert_to_int("123"))  
print(convert_to_int("abc"))  
