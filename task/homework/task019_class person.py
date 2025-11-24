class Person:


    def __init__(self):
        self.name = "Priyanshu"
        self.age = 45
        self.phone = 999958888
        self.occupation = "SDE"
        self.city = "Mumbai"

    def person_name(self):
        return self.name

    def person_age(self):
        return self.age

    def person_phone(self):
        return self.phone

    def person_occupation(self):
        return self.occupation

    def person_city(self):
        return self.city

Object_Ref = Person()
print(Object_Ref.person_name())
print(Object_Ref.person_age())
print(Object_Ref.person_phone())
print(Object_Ref.person_occupation())
print(Object_Ref.person_city())