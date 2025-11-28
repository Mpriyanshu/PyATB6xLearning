class InvalidAgeException(Exception):
    pass

def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")

def can_you_drink(age):
    if age < 18:
        raise Exception("Invalid age of Drinking")

can_you_drink(17)
can_you_drink(25)