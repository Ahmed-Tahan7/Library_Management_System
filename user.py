from person import Person
import json

class User(Person):
    def __init__(self, username: str, user_id: int, password: str):
        super().__init__(username, user_id)
        self.password = password

    def get_password(self) -> str:
        return self.password

    def set_password(self, new_password: str) -> None:
        self.password = new_password

    def save_to_json(self, file_path: str) -> None:
        user_data = {
            "username": self.username,
            "user_id": self.user_id,
            "password": self.password
        }
        with open(file_path, 'a') as json_file:
            json.dump(user_data, json_file)
            json_file.write('\n')

    @staticmethod
    def load_users_from_json(file_path: str) -> list:
        users = []
        with open(file_path, 'r') as json_file:
            for line in json_file:
                user_data = json.loads(line)
                user = User(user_data['username'], user_data['user_id'], user_data['password'])
                users.append(user)
        return users

    def __str__(self) -> str:
        return f"User({self.username}, {self.user_id})"

