import pandas as pd
from person import Person

class Admin(Person):
    def __init__(self, name, user_id, password):
        super().__init__(name, user_id, password)
    
    def get_info(self):
        return f"Username: {self.get_username()} | User ID: {self.get_user_id()} | Password: {self.get_password}"

def add_book(self, ISBN, title, author, genre, price, stock):
    try:
        books_df = pd.read_csv(self.books_file)
    except FileNotFoundError:
        books_df = pd.DataFrame(columns=['ISBN', 'Title', 'Author', 'Genre', 'Price', 'Stock'])
    except pd.errors.EmptyDataError:
        books_df = pd.DataFrame(columns=['ISBN', 'Title', 'Author', 'Genre', 'Price', 'Stock'])

    if ISBN in books_df['ISBN'].values:
        return f"Book with ISBN {ISBN} already exists in the stock."

    new_book = {
        'ISBN': ISBN,
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Price': price,
        'Stock': stock
    }

    books_df = books_df.append(new_book, ignore_index=True)
    books_df.to_csv(self.books.csv, index=False)

    print(f"Book '{title}' added to the stock.")


# Removes book from the books CSV file based on its ISBN
def remove_book(self, ISBN):
    try:
        books_df = pd.read_csv(self.books.csv)
    except FileNotFoundError:
        return "Books file not found"
    
    except pd.errors.EmptyDataError:
        return "Books file is empty or corrupted"

    if ISBN not in books_df['ISBN'].values:
        return f"Book with ISBN {ISBN} not found"

    books_df = books_df[books_df['ISBN'] != ISBN]
    print(f"Book with ISBN {ISBN} removed successfully")

    books_df.to_csv(self.books_file, index=False)

def update_book(self, ISBN, new_title=None, new_author=None, new_genre=None, new_price=None, new_stock=None):
    try:
        books_df = pd.read_csv(self.books.csv)
    except FileNotFoundError:
        return "Books.csv file not found"
    
    except pd.errors.EmptyDataError:
        return "Books.csv file is empty"

    if ISBN not in books_df['ISBN'].values:
        return f"Book with ISBN {ISBN} not found"
    
    book_index = books_df[books_df['ISBN'] == ISBN]
    
    if not book_index.empty:
        if new_title:
            books_df.loc[books_df['ISBN'] == ISBN, 'Title'] = new_title
        if new_author:
            books_df.loc[books_df['ISBN'] == ISBN, 'Author'] = new_author
        if new_genre:
            books_df.loc[books_df['ISBN'] == ISBN, 'Genre'] = new_genre
        if new_price:
            books_df.loc[books_df['ISBN'] == ISBN, 'Price'] = new_price
        if new_stock:
            books_df.loc[books_df['ISBN'] == ISBN, 'Stock'] = new_stock

        books_df.to_csv(self.books_file, index=False)
        print(f"Book with ISBN {ISBN} has been updated")
    else:
        print(f"Book with ISBN {ISBN} not found")

def view_all_books(self):
    books_df = pd.read_csv(self.books_file)
    return books_df
