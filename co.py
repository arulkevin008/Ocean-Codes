class data:
    def __init__(self,name,age,codeno):
        self.name=name
        self.age=age
        self.codeno=codeno

    def details(self):
        print(f"Name:{self.name},Age:{self.age},Codeno:{self.codeno}")

data1=data("Kevin",17,1254)
data2=data("Bhuvan",17,1236)
data3=data("Naren",17,1245)


print(data1.name)
print(data1.age)
print(data1.codeno)
data1.details()

print(data2.name)
print(data2.age)
print(data2.codeno)
data2.details()

print(data3.name)
print(data3.age)
print(data3.codeno)
data3.details()



