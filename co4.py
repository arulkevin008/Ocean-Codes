class smartphones:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def total(self):
        print(f"Brand:{self.brand},Model:{self.model}")

info=smartphones("Apple","Iphone16")
info1=smartphones("Samsung","S23")

print(info.brand)
print(info1.brand)
info.total()