def square_number():

    num = int(input("Enter a number: "))

    if num > 0:
        result = num**2
        print("Square of the number:", result)
    else:
        print("Please enter a positive number!")


square_number()

#Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

def triangle_type():
    # Taking input for sides
    side1 = int(input("Enter length of side 1: "))
    side2 = int(input("Enter length of side 2: "))
    side3 = int(input("Enter length of side 3: "))

    # Checking for triangle validity (triangle inequality)
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
        # Checking type of triangle
        if side1 == side2 == side3:
            result = "equilateral"       # Equilateral
        elif side1 == side2 or side2 == side3 or side1 == side3:
            result = "isosceles"      # Isosceles
        else:
            result = "scalene"  # Scalene
        print("Triangle type:", result)
    else:
        print("Invalid triangle sides!")

# Function call
triangle_type()
