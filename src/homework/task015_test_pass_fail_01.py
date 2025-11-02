status_code = int(input("Enter the status code:"))

def check_status(status_code):
    if status_code == 200:
        print("PASS")
    elif status_code == 400 or status_code == 500:
        print("FAIL")
    else:
        print("UNKNOWN")

result = check_status(status_code)
print(result)
