#Square all numbers in a list
def square(n):
    return n * n
n = [1, 2, 3, 4, 5]
squared_n = map(square, n)
print(list(squared_n))