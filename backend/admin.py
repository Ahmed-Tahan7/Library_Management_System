import pandas as pd
from backend.person import Person

class Admin(Person):
    """ Allows the admin to manage the inventory """

    def __init__(self, username, library_system):
        super().__init__(username, "admin", library_system)

    def add_book(self, book_details):
        
        try:
            book_id = int(book_details.get("book_id"))
        except (TypeError, ValueError):
            return "Book ID must be a valid integer"

        if book_id in self.library_system.books_df["book_id"].values:
            existing_book = self.library_system.books_df[
                self.library_system.books_df["book_id"] == book_id
            ].iloc[0]
            return f"Book ID {book_id} already exists for the book '{existing_book['title']}'"

        columns = ["book_id", "title", "author", "price", "quantity", "genre"]
        if self.library_system.books_df.empty:
            self.library_system.books_df = pd.DataFrame(columns=columns)

        new_book_df = pd.DataFrame([{col: book_details.get(col, None) for col in columns}])

        self.library_system.books_df["book_id"] = self.library_system.books_df["book_id"].astype(int)
        ids = self.library_system.books_df["book_id"].tolist()
        insert_pos = self.book_insertion(ids, book_id)

        self.library_system.books_df = pd.concat([
            self.library_system.books_df.iloc[:insert_pos],
            new_book_df,
            self.library_system.books_df.iloc[insert_pos:]
        ]).reset_index(drop=True)
        self.library_system.save_books("data/books.csv")
        return f"Book '{book_details['title']}' added successfully"

    def book_insertion(self, ids, book_id):

        low = 0
        high = len(ids)
        while low < high:
            mid = (low + high) // 2
            if ids[mid] < book_id:
                low = mid + 1
            else:
                high = mid
        return low

    def remove_book(self, title):
        
        title = title.strip().lower()
        book_row = self.library_system.books_df[
            self.library_system.books_df["title"].str.strip().str.lower() == title
        ]

        if book_row.empty:
            return f"Book titled '{title}' not found"

        self.library_system.books_df = self.library_system.books_df[
            self.library_system.books_df["title"].str.strip().str.lower() != title
        ]
        self.library_system.save_books("data/books.csv")
        return f"Book titled '{title}' removed successfully"

    def view_books(self):
        return self.library_system.books_df