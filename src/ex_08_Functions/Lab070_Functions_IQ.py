# Create a program to sum of three number from the user input
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/P AND O/P
# I/O - int
# O/P -   int

# STEP 2 -  Rough Logic
# return n1+n2+n3

# Step 3 - Write Logic

# num1 = int(input("Enter first number:\n "))
# num2 = int(input("Enter second number:\n "))
# num3 = int(input("Enter third number:\n "))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

# result = sum_of_three(num1, num2, num3)
result0 = sum_of_three(30, 40, 56)
result1 = sum_of_three()
result2 = sum_of_three(n1=10)
result3 = sum_of_three(n1=10, n2=30)
result4 = sum_of_three(n1=10, n2=30, n3=40)
#print(result)
print(result0)
print(result1)
print(result2)
print(result3)
print(result4)