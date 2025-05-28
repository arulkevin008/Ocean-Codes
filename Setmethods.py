#Difference
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
z=x.difference(y)
print(z)
z=y.difference(x)
print(z)

#Difference update
z=x.difference_update(y)
print(z)
x.difference_update(y)
print(x)
x={"apple", "banana", "cherry"}
y.difference_update(x)
print(y)

#Intersection
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)
z=y.intersection(x)
print(z)

#Intersection Update
x.intersection_update(y)
print(x)
x={"apple", "banana", "cherry"}
y.intersection_update(x)
print(y)

#issubset
x={"a", "b", "c"}
y={"f", "e", "d", "c", "b", "a"}
z=x.issubset(y)
print(z)
z=y.issubset(x)
print(z)
#issuperset
z=x.issuperset(y)
print(z)
z=y.issuperset(x)
print(z)

#Symmetric difference
x={"apple", "banana", "cherry"}
y={"google", "microsoft", "apple"}
z=x.symmetric_difference(y)
print(z)
z=y.symmetric_difference(x)
print(z)

#Symmetric difference update
x.symmetric_difference_update(y)
print(x)
x={"apple", "banana", "cherry"}
y.symmetric_difference_update(x)
print(y)