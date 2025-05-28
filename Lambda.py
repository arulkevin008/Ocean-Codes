x=lambda x:x**2
print(x(5))

y=lambda y:y+5
print(y(5))

def funct(x):
    return lambda n:n*2
mydoubler=funct(x)
print(mydoubler(5))

def func(x):
    return lambda n:n**2
mytripler=func(x)
print(mytripler(50))
    

