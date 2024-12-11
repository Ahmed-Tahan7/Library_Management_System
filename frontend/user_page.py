from tkinter import *
from tkinter import messagebox
from backend.library_system import LibrarySystem
from backend.user import User
class User_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.app = LibrarySystem()
        self.user = User(self.app.current_user, self.app)
        self.title("Library Management System / User")
        self.config(padx=150, pady=130, bg="#2e2e2e")
        
        self.screen = Text(state = DISABLED , width = 80, height = 20, bg = "#3c3c3c", fg = "white", insertbackground = "white", font = ("Helvetica", 12))
        self.screen.grid(column = 1, row = 0)

        self.search_entry = Entry(self, bg = "#3c3c3c", fg = "white", insertbackground = "white", font = ("Helvetica", 12))
        self.search_entry.place(x=160, y=380, width=300, height=30)


        self.add_button = Button(text = "Add Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.add_to_cart)
        self.cart_button = Button(text = "View Cart", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.view_cart)
        self.remove_button = Button(text = "Remove Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.remove_from_cart)
        self.logout_button = Button(text = "Logout", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command=self.handle_logout)
        self.search_button = Button(text="Search", bg="#2e2e2e", fg="white", highlightthickness=0, command=self.search_books)
        self.filter = StringVar(self, value="Title")
        filter_options = ["Title", "Author", "Genre"]
        filter_menu = OptionMenu(self, self.filter, *filter_options)
        filter_menu.config(bg="#2e2e2e", fg="white", highlightthickness=0)
        filter_menu.place(x=480, y=380, width=100, height=30)

        self.add_button.place(x=200, y=425, width=100, height=30)
        self.remove_button.place(x=350, y=425, width=100, height=30)
        self.cart_button.place(x=200, y=460, width=100, height=30)
        self.logout_button.place(x=350, y=460, width=100, height=30)
        self.search_button.place(x=480, y=425, width=100, height=30)


    def handle_logout(self):
        from frontend.login_page import Login_Gui
        self.back = LibrarySystem()
        self.back.logout()
        self.destroy()
        self.app = Login_Gui()

    def view_cart(self):
        cart_contents = self.user.view_cart()
        self.update_display(cart_contents)

    def search_books(self):
        search_term = self.search_entry.get()
        filter_option = self.filter.get().lower()
        results = self.app.search_books(search_term, filter_option)
        if results is None or results.empty:
            self.update_display("No books found matching your search.")
        else:
            self.update_display(results.to_string(index=False))

    def add_to_cart(self):
        title = self.get_selected_book_title()
        if not title:
            messagebox.showwarning("Warning", "Please enter a valid book title.")
            return
        title = title.strip().lower()
        result = self.user.add_to_cart(title, 1)
        messagebox.showinfo("Cart Update", result)

    def get_selected_book_title(self):
        return self.search_entry.get().strip()
    
    def remove_from_cart(self):
        title = self.get_selected_book_title()
        result = self.user.remove_from_cart(title)
        messagebox.showinfo("Cart Update", result)
        self.view_cart()

    def update_display(self, text):
        self.screen.config(state=NORMAL)
        self.screen.delete(1.0, END)
        self.screen.insert(END, text)
        self.screen.config(state=DISABLED)
