# Abstraction
# Hide the details and show what is required.

# Car - with key___private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Can -> driver -> Engine, gearbox?

from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog("PP")
dog.sound()

