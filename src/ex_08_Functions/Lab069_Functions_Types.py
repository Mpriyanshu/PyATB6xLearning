# User defined
# 1. They can't return -> non return
# 2. They can return something
# 3. They have parameters
# 4. They don't parameters / arguments

import math

# built in functions
result = max(3, 4)
print(result)


# 1. They can't return -> non return
# No Return Type and No Parameter / Argument - NRNP

def greet():
    print("Hello")


greet()


# 2. No return type and with argument/ para

def greet_by_name(name):
    print("Hello", name)


greet_by_name("Priyanshu")


# 3. No Return Type and with Default Argument ( # positional arg

def say_hello_default_arg(name="Piyanshu"):
    print("Hello", name.upper())


say_hello_default_arg("Tiwari")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print("Mul ->", name1, name2)


multiple_args()
multiple_args(name1="Radha", name2="Krishna")
multiple_args(name1="Ram")
multiple_args(name1="Shiv", name2="Parvati")
multiple_args(name1="Sita")


# def test(name):
#    return name
# test("test")

# 4. Argument + Return Type

def sum_of_two(a, b):
    return a + b


result = sum_of_two(1, 2)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)


