#Random module
import random
print(random.random()*10)
print(random.randint(0,5))
print(random.uniform(0,5))
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
print(random.choices(mylist))
print(random.sample(mylist, k=2))
random.shuffle(mylist)
print(mylist)
