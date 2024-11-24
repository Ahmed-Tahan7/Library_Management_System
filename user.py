from person import Person
import json

class User(Person):
    def __init__(self, username, user_id, password, cart):
        super().__init__(username, user_id, password)
        self.cart = cart

    def get_info(self):
        return f"Username: {self.get_username()} | User ID: {self.get_user_id()} | Password: {self.get_password}"
    
    file_path = "loginDetails.json"
    
    def save_to_json(self, file_path):
        user_data = {
            "username": self.get_username(),
            "user_id": self.get_user_id(),
            "password": self.get_password()
        }

        with open(file_path, 'a') as json_file:
            json.dump(user_data, json_file)
            json_file.write('\n')

    @staticmethod
    def load_users_from_json(file_path) -> list:
        users = []
        with open(file_path, 'r') as json_file:
            for line in json_file:
                user_data = json.loads(line)
                user = User(user_data['username'], user_data['user_id'], user_data['password'])
                users.append(user)
        return users

    def get_info(self):
        return

