def fibonacci_sequence(series):
    results = []
    a, b = 0, 1
    while a <= series:
        results.append(a)
        a, b = b, a + b
    print(results)
series = 50
fibonacci_sequence(series)