class InvalidAgeException(Exception):
    pass

def can_you_drink(age):
    if age < 18:
        raise Exception("Invalid age of Drinking")

can_you_drink(25)