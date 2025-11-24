class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

Object_Ref = Calc(5,7)
print(Object_Ref.sum())
print(Object_Ref.mul())