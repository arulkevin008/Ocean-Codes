def even(n):
    return (n,"Even") if n%2==0 else (n,"Odd")
n = [1, 2, 3, 4, 5]
even_n = map(even, n)
print(list(even_n))