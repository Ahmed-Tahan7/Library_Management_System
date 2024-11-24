import pandas as pd
import json
from user import User

class Library_Manager:
    _instance = None

    def __new__(cls, books_file=None, users_file=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, books_file=None, users_file=None):
        if not self._initialized:
            self.books_file = books_file
            self.users_file = users_file
            self.books = {}
            self.users = {}
            self._initialized = True

    # Load books from the CSV file into the dictionary
    def load_books(self):
        df = pd.read_csv(self.books_file)
        self.books = {row['ISBN']: Book(row['ISBN'], 
                                        row['Title'], 
                                        row['Author'], 
                                        row['Genre'], 
                                        row['Price'], 
                                        row['Stock'])
                      for _, row in df.iterrows()}

    # Save the current books dictionary to the CSV file
    def save_books(self):
        df = pd.DataFrame([vars(book) for book in self.books.values()])
        df.to_csv(self.books_file, index=False)

    # Load users from the JSON file into the dictionary
    def load_users(self):
        with open(self.users_file, 'r') as file:
            data = json.load(file)
            self.users = {user_data['user_id']: User.from_dict(user_data) 
                          for user_data in data}

    # Save the current users dictionary to the JSON file
    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users.values()], file)

    # Find a book using its ISBN with O(1) complexity
    def find_book(self, ISBN):
        return self.books.get(ISBN)

    # Find a user using their id with O(1) complexity
    def find_user(self, user_id):
        return self.users.get(user_id)
