# Problem Find the Max between 3 numbers

# Logic Building

# User inputs - numl, num2, num3 -> int
# O/p -> int or String with max number.

num1 = int(input("Enter the num1: ")) #5, #10
num2 = int(input("Enter the num2: ")) #3, #12
num3 = int(input("Enter the num3: ")) #2, #11

# 5 > 3 and 5 >2 -> 5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 and num2 > num3 -> num2
# num3 - max

if num1 >= num2 and num1 >= num3 :
    print("max",num1)
elif num2 >= num3 and num2 >= num1:
    print("max",num2)
else:
    print("max",num3)