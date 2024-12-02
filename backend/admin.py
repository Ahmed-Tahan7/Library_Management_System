import pandas as pd
from backend.person import Person

class Admin(Person):
    """ Allows the admin to manage the inventory """

    def __init__(self, username, library_system):
        super().__init__(username, "admin", library_system)

    def add_book(self, book_details):
        # book_details (dict): A dictionary containing book information
        
        book_id = book_details.get("book_id")
        if book_id in self.library_system.books_df["book_id"].values:
            return f"Book ID {book_id} already exists."

        columns = ["book_id", "title", "author", "price", "quantity", "genre"]
        if self.library_system.books_df.empty:
            self.library_system.books_df = pd.DataFrame(columns=columns)

        new_book_df = pd.DataFrame([{col: book_details.get(col, None) for col in columns}])

        self.library_system.books_df = pd.concat(
            [self.library_system.books_df, new_book_df], ignore_index=True
        )
        
        self.library_system.save_books("data/books.csv")
        return f"Book '{book_details['title']}' added successfully"

    def remove_book(self, book_id):
        if book_id not in self.library_system.books_df["book_id"].values:
            return f"Book ID: {book_id} not found"
    
        self.library_system.books_df = self.library_system.books_df[
            self.library_system.books_df["book_id"] != book_id
        ]
        self.library_system.save_books("data/books.csv")
        return f"Book with ID {book_id} removed successfully"

    def view_books(self):
        return self.library_system.books_df