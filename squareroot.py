import math

def safe_sqrt(n):
    try:
        if n < 0:
            raise ValueError("Negative input")
        return math.sqrt(n)
    except ValueError as e:
        return str(e)
print(safe_sqrt(9))   
print(safe_sqrt(-1)) 
