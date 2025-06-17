#Hybrid Inheritance
class A:
    def show_A(self):
        print("class A")

class B(A):
    def show_B(self):
        print("class B")

class C(A):
    def show_C(self):
        print("class C")

class D(B, C): 
    def show_D(self):
        print("class D")

d_obj = D()

d_obj.show_A()  
d_obj.show_B()  
d_obj.show_C()  
d_obj.show_D()  