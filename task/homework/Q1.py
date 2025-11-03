Api_response = int(input("Enter response:\n").strip())

if Api_response == 200 :
    print("Passed API Request")
elif Api_response == 400:
    print("Failed API Request")
else:
     print("valid API Request")
