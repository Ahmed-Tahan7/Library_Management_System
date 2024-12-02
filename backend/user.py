from backend.person import Person

class User(Person):
    """
    Handle user in the Library Management System, 
    allows him to search, filter books, and manage his cart
    """
    
    def __init__(self, username, library_system):
        super().__init__(username, "user", library_system)
        self.cart = {}  # {book_id: quantity}

    def add_to_cart(self, book_id, quantity):
        # Find the book by ID in the inventory
        book_row = self.library_system.books_df[self.library_system.books_df["book_id"] == book_id]
        if book_row.empty:
            return "Book not found"
        
        book_index = book_row.index[0] 
        book = book_row.iloc[0]

        # Check quantity if available
        if book["quantity"] >= quantity:
            self.cart[book_id] = self.cart.get(book_id, 0) + quantity
            self.library_system.books_df.at[book_index, "quantity"] -= quantity
            self.library_system.save_books("data/books.csv")
            return f"Added {quantity} of '{book['title']}' to the cart"
        else:
            return f"Not enough stock available for '{book['title']}'"


    def remove_from_cart(self, book_id):
        if book_id in self.cart:
            del self.cart[book_id]
            return "Book removed from cart"
        return "Book not found in cart"

    def view_cart(self):
        if not self.cart:
            return "Your cart is empty"
        
        cart_summary = []
        for book_id, quantity in self.cart.items():
            book = self.library_system.books_df[self.library_system.books_df["book_id"] == book_id].iloc[0]
            cart_summary.append(f"{book['title']} x{quantity}")
        return "\n".join(cart_summary)

    def view_books(self):
        return self.library_system.books_df[self.library_system.books_df["quantity"] > 0]
    
