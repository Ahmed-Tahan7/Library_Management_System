from tkinter import *
from backend.library_system import LibrarySystem
from backend.admin import Admin
class Admin_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System / Admin")
        self.app = LibrarySystem()
        self.admin = Admin(self.app.current_user, self.app)
        self.config(padx=150, pady=130, bg="#2e2e2e")
        
        self.screen = Text(state = DISABLED , width = 80, height = 20, bg = "#3c3c3c", fg = "white", insertbackground = "white", font = ("Helvetica", 12))
        self.screen.grid(column = 1, row = 0)

        self.search_entry = Entry(width = 30, bg = "#3c3c3c", fg = "white", insertbackground = "white", font = ("Helvetica", 12))
        self.search_entry.place(x=160, y=380, width=300, height=30)

        self.add_button = Button(text = "Add Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.add_book)
        self.inventory_button = Button(text = "Inventory", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.view_inventory)
        self.remove_button = Button(text = "Remove Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.remove_book)
        self.logout_button = Button(text = "Logout", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command = self.handle_logout)
        self.search_button = Button(text = "Search", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.search_books)
        
        self.add_button.place(x=200, y=425, width=100, height=30)
        self.remove_button.place(x=350, y=425, width=100, height=30)
        self.inventory_button.place(x=200, y=460, width=100, height=30)
        self.logout_button.place(x=350, y=460, width=100, height=30)
        self.search_button.place(x=480, y=380, width=100, height=30)

        self.books_dict = {}

    def handle_logout(self):
        from backend.library_system import LibrarySystem
        from frontend.login_page import Login_Gui
        self.back = LibrarySystem()
        self.back.logout()
        self.destroy()
        self.app = Login_Gui()

    def search_books(self):
        search_term = self.search_entry.get()
        filter_option = None
        results = self.app.search_books(search_term, filter_option)
        if results is None or results.empty:
            self.update_display("No books found matching your search.")
        else:
            self.update_display(results.to_string(index=False))

    def view_inventory(self):
        inventory_contents = self.admin.view_books()
        self.update_display(inventory_contents)

    def update_display(self, text):
        self.screen.config(state=NORMAL)
        self.screen.delete(1.0, END)
        self.screen.insert(END, text)
        self.screen.config(state=DISABLED)

    def get_selected_book_id(self):
        return self.search_entry.get().strip()
    
    def remove_book(self):
        book_id = int(self.get_selected_book_id())
        result = self.admin.remove_book(book_id)
        self.update_display(result)

    def book_details(self):
            book_details = self.search_entry.get()
            try:
                details = book_details.split(",")
                if len(details) != 6:
                    raise ValueError("Please enter the details in the correct format: Book ID, Title, Author, Price, Quantity, Genre.")
                book_id, title, author, price, quantity, genre = details[0].strip(), details[1].strip(), details[2].strip(), details[3].strip(), details[4].strip(), details[5].strip()
                return {
                    "book_id": book_id,
                    "title": title,
                    "author": author,
                    "price": price,
                    "quantity": quantity,
                    "genre": genre
                }
            except Exception as e:
                self.update_display(f"Error: {str(e)}")

    def add_book(self):
        book_data = self.book_details()
        if book_data:
            result = self.admin.add_book(book_data)
            self.update_display(result)
            self.search_entry.delete(0, END)