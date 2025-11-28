
try:
    a = int(input("Enter num 1:"))
    b = int(input("Enter num 2:"))
    c = a/b
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zero division error")
else: # Runs only if try block succeeds
    print(c)
finally:
    print("I will always execute!")

