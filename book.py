import pandas as pd

class Book:
    def __init__(self, title: str, author: str, genre: str, price: float, isbn: str):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.isbn = isbn

    def save_to_csv(self, file_path: str) -> None:
        df = pd.DataFrame({
            "Title": [self.title],
            "Author": [self.author],
            "Genre": [self.genre],
            "Price": [self.price],
            "ISBN": [self.isbn]
        })
        df.to_csv(file_path, mode='a', header=False, index=False)

    @staticmethod
    def load_books_from_csv(file_path: str) -> list:
        df = pd.read_csv(file_path)
        books = []
        for index, row in df.iterrows():
            book = Book(row['Title'], row['Author'], row['Genre'], row['Price'], row['ISBN'])
            books.append(book)
        return books

    def __str__(self) -> str:
        return f"Book({self.title}, {self.author}, {self.genre}, {self.price}, {self.isbn})"
