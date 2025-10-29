# Write a program to take a user age and
# let him know if he can go the club.
# 21

# logic Building Formula

# Step 1
# i/p - age, int
# o/p - string (Result -> can go to club or  not.

# Step 2. Rough Logic ( Brute force)
"""
age > 21 -> print can go
age < 21 -> print can't go

"""
# Step 3. Write the logic

age = int(input("Enter age:\n"))
if age >= 21:
    print("Yes, can go club")
else:
    print("No, can't go club.")

# Step 4. Check for the Edge cases
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break
# Non-numeric input - ABC
# Age which is valid. > 130

# Step 5. Optimize the code.
# Handle all the edges.