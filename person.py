class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, email, password):
        return self.email == email and self.password == password
