class Home:
     def __init__(self):
         self.public_var = "father"
         self.__private_var = "baby"

        def mom(self):
            print(self.__private_var)
            self.wife()

        def __wife(self):
            print("Private Wife")


object_ref = Home()
#object_ref.__wife()
#object_ref.__private_var