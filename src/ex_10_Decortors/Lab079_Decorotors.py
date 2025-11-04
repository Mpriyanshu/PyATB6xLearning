def add_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2. Add Helmet, Dashcash, gloves, knee guards, Licience")
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, leave all the items")

    return wrapper()







@add_security
def drive_ola_scooter():
    print("I Am Driving ola scooter!")

@add_security
def drive_zypp_scooter():
    print("Driving zypp scooter!")