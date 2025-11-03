#I/p

#username = "admin"
#password = "1234"

username= input("Enter the admin credentials:").strip()
password =input("Enter the password credentials:").strip()

if username.lower() == "admin" and password == "1234":
    print("login successful")
else:
    print("Invalid credentials")