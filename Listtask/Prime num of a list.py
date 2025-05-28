#Prime num of a List
List=[1,2,3,4,5,6,7,8,9]
primes = []
for x in List:
    if x > 1:
        is_prime = True
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
print(primes)