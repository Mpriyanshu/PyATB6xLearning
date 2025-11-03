#expected_title ="Dashboard"
#actual_title ="dashboard"

expected_title = input("enter the expected title: ").strip()
actual_title = input("enter the actual title: ").strip()

if expected_title.lower() == actual_title:
    print("The test is passed - title matches")
else:
    print("The test is Failed - title does not matches")