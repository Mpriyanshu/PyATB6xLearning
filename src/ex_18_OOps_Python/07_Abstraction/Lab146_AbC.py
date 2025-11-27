from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @adstractmethod 
    def loan(self):
        pass

class Amit(Father):
    def loan(self):
        print("Giving the 50k loan")

amit = Amit("AMIT SHARMA")
amit.loan()

