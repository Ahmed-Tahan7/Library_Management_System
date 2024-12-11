from backend.person import Person

class User(Person):
    """
    Handle user in the Library Management System, 
    allows him to search, filter books, and manage his cart
    """
    
    def __init__(self, username, library_system):
        super().__init__(username, "user", library_system)
        self.cart = {}  # {book_id: quantity}

    def add_to_cart(self, title, quantity):
        # Normalize the title for case-insensitive and whitespace-free comparison
        title = title.strip().lower()
        
        # Find the book by title in the inventory (normalize the titles in the DataFrame as well)
        book_row = self.library_system.books_df[self.library_system.books_df["title"].str.strip().str.lower() == title]
        
        if book_row.empty:
            return "Book not found"
        
        book_index = book_row.index[0] 
        book = book_row.iloc[0]

        # Check if enough quantity is available
        if book["quantity"] >= quantity:
            self.cart[title] = self.cart.get(title, 0) + quantity
            self.library_system.books_df.at[book_index, "quantity"] -= quantity
            self.library_system.save_books("data/books.csv")
            return f"Added {quantity} of '{book['title']}' to the cart"
        else:
            return f"Not enough stock available for '{book['title']}'"

    def remove_from_cart(self, title):
        if title in self.cart:
            del self.cart[title]
            return "Book removed from cart"
        return "Book not found in cart"

    def view_cart(self):
        if not self.cart:
            return "Your cart is empty"
        
        cart_summary = []
        for title, quantity in self.cart.items():
            # Normalize the title for case-insensitive and whitespace-free comparison
            title = title.strip().lower()
            
            # Find the book by normalized title in the inventory
            book_row = self.library_system.books_df[self.library_system.books_df["title"].str.strip().str.lower() == title]
            
            if not book_row.empty:
                book = book_row.iloc[0]
                cart_summary.append(f"{book['title']} x{quantity}")
            else:
                cart_summary.append(f"Book '{title}' not found in inventory.")
        
        return "\n".join(cart_summary)

    def view_books(self):
        return self.library_system.books_df[self.library_system.books_df["quantity"] > 0]

    def checkout(self):
        if not self.cart:
            return "Your cart is empty. Please add items before checking out."
        total_price = 0
        checkout_summary = []
        for title, quantity in self.cart.items():
            title = title.strip().lower()
            book_row = self.library_system.books_df[self.library_system.books_df["title"].str.strip().str.lower() == title]
            if not book_row.empty:
                book = book_row.iloc[0]
                book_price = book["price"] * quantity
                total_price += book_price
                checkout_summary.append(f"{book['title']} x{quantity} - ${book_price:.2f}")
            else:
                checkout_summary.append(f"Book '{title}' not found in inventory (skipped).")
        self.cart.clear()
        return f"Checkout Summary:\n" + "\n".join(checkout_summary) + f"\n\nTotal Price: ${total_price:.2f}"