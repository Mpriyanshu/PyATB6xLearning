
try:
    a = int(input("Enter num 1:"))
    b = int(input("Enter num 2:"))
    c = a/b
    print(c)
except (NameError, ValueError, ZeroDivisionError):
    print("Error Due to the Type,Name, Value,  or Zero Div")
