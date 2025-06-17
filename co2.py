class color:
    def __init__(self,name,color,rupees):
        self.name=name
        self.color=color
        self.rupess=rupees

    def bill(self):
        print(f"Name:{self.name},Color:{self.color},Rupess:{self.rupess}")
    
fruits=color("Apple","Red",30)
fruits1=color("Banana","Yellow",20)

print(fruits.name)
print(fruits.color)
print(fruits.rupess)
fruits.bill()

print(fruits1.name)
print(fruits1.color)
print(fruits1.rupess)
fruits1.bill()

    