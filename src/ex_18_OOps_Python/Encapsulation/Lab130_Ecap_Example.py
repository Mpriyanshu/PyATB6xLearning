# Encapsulation
# Hide the data members(class Variables, instance variables)
# by using only the methods
import os


class Car:

    def __init__(self):
        self.public_me = "Aman"
        self.__private_baby = "pass123"

    def nany(self):
        self.__password_aman_private = "123"

object_ref = Car()

print(object_ref.public_me)
print(object_ref.__private_baby)

object_ref.nany()