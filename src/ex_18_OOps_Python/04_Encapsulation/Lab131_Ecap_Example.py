class Bank:

    def __init__(self,account_number, balance):
        self.balance = balance # Public
        self.__account_number = account_number #Private

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")


icici = Bank("789456123",100)
icici.deposit(100)
icici.check_balance()
# print(icici.account_number) -> Not allowed directly
# if you are cashier you can see the a/c becoz of the encapsulation
icici.show_me_account_number(True)
