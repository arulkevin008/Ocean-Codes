#Single Inheritance
class A:
    def a(self):
        print("Class A")

class B(A):
    def b(self):
        print("Class B")

Bobj=B()
Bobj.a()
Bobj.b()

