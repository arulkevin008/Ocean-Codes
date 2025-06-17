#Hierarchical Inheritance
class A:
    def a(self):
        print("Class A")

class B(A):
    def b(self):
        print("Class B")

class C(A):
    def c(self):
        print("Class C")

Cobj=C()
Bobj=B()
Cobj.a()
Bobj.b()
Cobj.c()
