def validate_Status_code(response_code):
    response_code = int(response_code)
    if response_code > 0:
        if response_code == 200:
            print("Request is Success")
        else:
            print("Error is the Request")
    else:
        print("Error is the Response code value.")


validate_Status_code(404)
validate_Status_code(200)
validate_Status_code(response_code=200)
validate_Status_code(input("Enter your status code:"))
