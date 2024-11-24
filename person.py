from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, username, user_id, password):
        self.__username = username
        self.__user_id = user_id
        self.__password = password

    @abstractmethod
    def get_info(self):
        pass

    def get_username(self):
        return self.__username
    
    def set_username(self, new_username):
        self.__username = new_username

    def get_user_id(self):
        return self.__user_id
    
    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password

     
