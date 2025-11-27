""" Goal:

Create a simple automation structure that uses:

A BaseTest class for setup/teardown (Parent class)

A LoginTest class that inherits BaseTest (Child class)

Encapsulate sensitive data (like credentials) as private variables
"""


class BaseTest:
    _driver = "Chrome"

    def setup(self):
        print("Launching Browser"+ self._driver)

    def teardown(self):
        print("Closing Browser")

class LoginTest(BaseTest):
    __username = "admin"

    def run_test(self):
        self.setup()
        print("Running login test with user:-" + self.__username)

obj_ref = LoginTest()
obj_ref.run_test()
obj_ref.teardown()