import requests
from random import  randint
class Person():
    def __init__(self, name="",surname="", login="", password=""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.__lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sit amet placerat nisi. Donec id orci nec enim pulvinar pellentesque. Ut in rutrum leo, at ultricies nisl. Ut eleifend arcu a dolor pellentesque, vel faucibus dolor laoreet. Sed sapien sapien, congue at imperdiet eu, elementum non sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer in massa non nunc ultrices cursus vitae ac felis. Curabitur.'
        print(self.__data)
        self.name = self.__data['FirstName'] if not name else name
        self.surname = self.__data['LastName'] if not surname else surname
        self.login = self.__data['Login'] if not login else login
        self.__password = self.__data['Password'] if not password else password
        self.subsscribers = []
        self.subscribe = []
        self.posts = [self.__lorem[randint(1,20):randint(20,40)] for i in range(randint(1,10))]
    def log_in(self,login, password):
        if login == self.login and password == self.__password:
            return True
        else:
            return False
