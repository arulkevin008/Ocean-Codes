#Multiple Inheritance
class A:
    def a(self):
        print("Class A")

class B():
    def b(self):
        print("Class B")

class C(B,A):
    def c(self):
        print("Class C")

Cobj=C()
Cobj.a()
Cobj.b()
Cobj.c()
