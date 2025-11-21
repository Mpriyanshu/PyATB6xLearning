a = 10
class Person:
    b = 11 # instance Variable

    def print_info(self):
        c = 20 # Local Variable
        print(c)
        print(self.b)
        print(a)

object_ref = Person()