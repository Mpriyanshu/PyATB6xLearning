class BaseTest:
    def run(self):
        print("Running generic test")

class LoginTest(BaseTest):
    def run(self):
        print("Running login test")

#t = LoginTest()
t = BaseTest()
t.run()