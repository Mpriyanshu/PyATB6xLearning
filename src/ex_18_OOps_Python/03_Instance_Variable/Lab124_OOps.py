a = 10 # Variable everywhere in the program
class Person:
    b = 11 # instance Variable

    def print_info(self):
        c = 20 # Local Variable
        print(c)
        print(self.b)
        print(a)

object_ref = Person()
#print(b)
#print(c)