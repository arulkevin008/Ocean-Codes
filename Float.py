def parse_float(s):
    try:
        return float(s)
    except ValueError:
        return "Invalid float"
print(parse_float("3.14"))  
print(parse_float("abc"))   
