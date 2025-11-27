class Base:
    def base_method(self):
        print("Base Method")


class A(Base):
    def a_method(self):
        print("A method")

class B(Base):
    def b_method(self):
        print("B method")

class C(A, B): # Multiple
    def c_method(self):
        print("C method")

obj = C()
obj.a_method()
obj.b_method()
obj.c_method()