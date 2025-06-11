def function(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@function
def decorator():
    a=10
    b=10
    print(a+b)
decorator()