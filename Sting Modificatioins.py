#Access using Index

a="Hello"
print(a[2])
print(a[0])
print(a[1])

#Find length of str

a="Hello"
print(len(a))

#Loop using string

a="Hello"
for i in a:
    print(i)

#In,not in

a="Welcome to Python"
print("Python"in a)
print("Python"not in a)

#String Slicing

a="Hello"
print(a[2:5])
print(a[0:])
print(a[:2])

#upper,lower

a="Hello"
print(a.upper())
print(a.lower())

#Strip
a=" Hello World "
print(a.strip())

#replace
print(a.replace("H","h"))

#split
a="OCNSY-16"
print(a.split("-"))
