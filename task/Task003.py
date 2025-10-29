# Write a Python program to calculate the
# area of a circle given its radius using the formula
# '''area=π*r^2''' (take pie as 3.14)
import math
# i/p - r - float
# o/p -> String formatted output of area

# Logical Building Formula
# // STEP1 //
# Figure out the input and output
# input -> r -> data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> String -> float - area, print area

# // Step 2 //
# rough logic = area = 3.14 * pow(r,2)

# // step 3 //
radius = float(input("Enter radius of the circle:\n"))
print(radius)
#area = 3.14987654 * (radius**2)
area = math.pi * (pow(radius, 2))

print("Area of circle is:", area)

# string data formatting, Python f-strings, Formatted string literals
print(f"Area of circle is:{area:.2f}")

