class Person:
    def __init__(self, username, user_id, password):
        self.username = username
        self.user_id = user_id
        self.password = password

    def get_info(self):
        return f"Username: {self.username}, User ID: {self.user_id}"
