class TestExample:

    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api__key = "ABC12345"

    def show(self):
        print(f"Driver, {self.driver}")
        print(f"Config, {self._config}")
        print(f"API, {self.__api__key}")

    def __private_method1(self):
        pass

    def _private_method2(self):
        pass

    def work(self):
        pass

    def work2(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()
obj.work()

# Access levels:
# print(obj.driver)          # Public - accessible
# print(obj ._config)       # A Protected - accessible but discouraged
# print(obj .__api __ key)   # X Private - AttributeError


