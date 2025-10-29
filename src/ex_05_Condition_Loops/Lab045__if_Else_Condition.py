# Problem to find the max between two.

# Logic Building Formula

# 1. user inputs -> two integers
# 2. o/ p —> int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#if num1 > 0 and num2 > 0:
#    print("Number should be positive")


if num1 > num2:
    print("Maximun", num1)
else:
    print("Maximum", num2)

# num1 == num2 -> Handled.

