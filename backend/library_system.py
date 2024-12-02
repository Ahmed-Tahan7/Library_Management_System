library_system.py

from backend.admin import Admin
from backend.user import User
import pandas as pd
import json

class LibrarySystem:
    """ Manages Library Management System's backend logic (user authentication, inventory, file operations) """

    # Singleton
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LibrarySystem, cls).__new__(cls)
        return cls._instance

    def __init__(self, cipher):
        # Prevent re-initialization in Singleton
        if not hasattr(self, 'initialized'):  
            self.cipher = cipher
            self.users_df = None
            self.books_df = None
            self.current_user = None
            self.load_users("data/loginDetails.json")
            self.load_books("data/books.csv")
            self.initialized = True

    def load_users(self, data_file):
        try:
            with open(data_file, "r") as file:
                data = json.load(file)
            for user in data:
                user["password"] = self.cipher.decrypt(user["password"])
            self.users_df = pd.DataFrame(data)
        except FileNotFoundError:
            print(f"Error: {data_file} not found")
            self.users_df = pd.DataFrame(columns=["username", "password", "role"])
        except json.JSONDecodeError:
            print(f"Error: {data_file} contains invalid JSON")
            self.users_df = pd.DataFrame(columns=["username", "password", "role"])

    def save_users(self, data_file):
        data = self.users_df.to_dict(orient="records")
        for user in data:
            user["password"] = self.cipher.encrypt(user["password"])
        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

    def login(self, username, password):        
        encrypted_password = self.cipher.encrypt(password)
        # print(f"Enc password={encrypted_password}")
        user_row = self.users_df[
            (self.users_df["username"] == username) & 
            (self.users_df["password"] == encrypted_password)
        ]
        if not user_row.empty:
            role = user_row.iloc[0]["role"]
            if role == "admin":
                self.current_user = Admin(username, self)
            elif role == "user":
                self.current_user = User(username, self)
            return True
        return False, "Login failed! User not found!"

    def logout(self):
        self.current_user = None

    def add_new_user(self, username, password):
        if username in self.users_df["username"].values:
            return "User already exists"
        new_user = {
            "username": username, 
            "password": self.cipher.encrypt(password), 
            "role": "user"
        }
        self.users_df = pd.concat([self.users_df, pd.DataFrame([new_user])], ignore_index=True)
        self.save_users("data/loginDetails.json")
        return "User added successfully"

    # -------- Book Inventory Management --------
    def load_books(self, data_file):
        columns = ["book_id", "title", "author", "price", "quantity", "genre"]
        try:
            self.books_df = pd.read_csv(data_file)
            if self.books_df.empty:
                self.books_df = pd.DataFrame(columns=columns)
                return f"Warning: {data_file} is empty"
        except FileNotFoundError:
            self.books_df = pd.DataFrame(columns=columns)
            return f"Error: {data_file} not found"
        except pd.errors.EmptyDataError:
            self.books_df = pd.DataFrame(columns=columns)
            return f"Error: {data_file} is empty"

    def save_books(self, data_file):
        self.books_df.to_csv(data_file, index=False)
        
    # -------- Book Search and Filtering --------
    def search_books(self, search_input, filter_option):
        search_input = str(search_input).strip()

        if not search_input:
            return self.books_df

        filter_option = filter_option.lower() if filter_option else "none"
        if filter_option == "none":
            return self.books_df[
                self.books_df["title"].str.contains(search_input, case=False, na=False) |
                self.books_df["author"].str.contains(search_input, case=False, na=False) |
                self.books_df["genre"].str.contains(search_input, case=False, na=False)
                ]
        elif filter_option == "title":
            return self.books_df[self.books_df["title"].str.contains(search_input, case=False, na=False)]
        elif filter_option == "author":
            return self.books_df[self.books_df["author"].str.contains(search_input, case=False, na=False)]
        elif filter_option == "genre":
            return self.books_df[self.books_df["genre"].str.contains(search_input, case=False, na=False)]
