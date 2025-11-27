class BaseAPI:
     __token = "ABC123SECRET"
     def gettoken(self):
         return self.__token

class UserAPI(BaseAPI):
     def get_user_data(self):
         print("Fetching user data using token:-", self.gettoken())


obj = UserAPI()
obj.get_user_data()