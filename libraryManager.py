import pandas as pd
import json
from book import Book
from user import User
class Library_Manager:
    def __init__(self, books_file, users_file):
        self.books_file = books_file
        self.users_file = users_file
        self.books = {}
        self.users = []

    def load_books(self):
        df = pd.read_csv(self.books_file)
        for index, row in df.iterrows():
            book = Book(row['ISBN'], row['Title'], row['Author'], row['Genre'], row['Price'], row['Stock'])
            self.books[book.ISBN] = book

    def save_books(self):
        df = pd.DataFrame([vars(book) for book in self.books.values()])
        df.to_csv(self.books_file, index=False)

    def load_users(self):
        with open(self.users_file, 'r') as file:
            data = json.load(file)
            self.users = [User.from_dict(user_data) for user_data in data]

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def add_book(self, book):
        self.books[book.ISBN] = book
        self.save_books()

    def add_user(self, user):
        self.users.append(user)
        self.save_users() 

    def find_book(self, ISBN):
        return self.books.get(ISBN, None)

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
