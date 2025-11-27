class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name" + self.name)
        print("Starting a car with the make" + self.make)
        print("Starting a car with the model" + self.model)

lambo = Car(o_name="lambo", o_make="V6", o_model="2023")
lambo.start_engine()

mg_hector = Car(o_name="Hector", o_make="1.5+Turbo", o_model="2023")
mg_hector.start_engine()