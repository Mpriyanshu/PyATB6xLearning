class Person:
    # Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    # Behaviour
    def talk(self): # self - this, self will be the first argument in every behaviour
        print("I can Talk")


    def sleep(self, name): # Arg with No return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name): # Arg with return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am Walking")

    def walk_return(self): # No Arg with return
        return "I am Walking"

def outside():
    print("outside")

# Create an object of the class
# ObjectRef = ClassName() -> Object
geeta = Person()
print(geeta.name) # - Atri
geeta.sleep("Priyanshu") # - Bheva
