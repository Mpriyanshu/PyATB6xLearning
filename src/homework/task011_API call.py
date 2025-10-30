# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# Test Passed

API_Call = 0
while API_Call < 3:
    number = int(input("Enter a number: "))
    if number == 200:
        print("Test Passed",number)
        break
    elif number != 200:
        print("No response",number)
        API_Call +=1
if API_Call == 3:
        print("Test Failed",number)

