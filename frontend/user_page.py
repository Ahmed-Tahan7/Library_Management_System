from tkinter import *
import tkinter as tk
from tkinter import messagebox
from backend.library_system import LibrarySystem
from backend.user import User
from backend.admin import Admin

class User_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.app = LibrarySystem()
        self.user = User(self.app.current_user, self.app)
        self.title("Library Management System / User")
        self.config(padx=120, pady=180, bg="#2e2e2e")

        self.title_label = Label(text=f"Welcome to The Whispering Pages Bookstore - {self.app.current_user.username.capitalize()}", bg="#2e2e2e", fg="white", highlightthickness=0, font=("Helvetica", 18))
        self.title_label.grid(column=1, row=0)

        self.books_display = Text(state=DISABLED, width=105, height=20, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.books_display.grid(column=1, row=1)

        self.search_entry = Entry(self, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.search_entry.place(x=180, y=380, width=300, height=30)

        self.add_button = Button(text="Add Book", bg="#28a745", fg="white", highlightthickness=0, command=self.add_to_cart)
        self.cart_button = Button(text="View Cart", bg="#6c757d", fg="white", highlightthickness=0, command=self.view_cart)
        self.remove_button = Button(text="Remove Book", bg="#dc3545", fg="white", highlightthickness=0, command=self.remove_from_cart)
        self.checkout_button = Button(text="Checkout", bg="#e8590c", fg="white", highlightthickness=0, command=self.checkout)
        self.search_button = Button(text="Search", bg="#007bff", fg="white", highlightthickness=0, command=self.search_books)
        self.logout_button = Button(text="Logout", bg="#a71e2a", fg="white", highlightthickness=0, command=self.handle_logout)

        self.filter = StringVar(self, value="Title")
        filter_options = ["Title", "Author", "Genre"]
        filter_menu = OptionMenu(self, self.filter, *filter_options)
        filter_menu.config(bg="#2e2e2e", fg="white", highlightthickness=0)
        filter_menu.place(x=500, y=380, width=100, height=30)

        self.add_button.place(x=220, y=425, width=100, height=30)
        self.remove_button.place(x=370, y=425, width=100, height=30)
        self.cart_button.place(x=220, y=460, width=100, height=30)
        self.checkout_button.place(x=370, y=460, width=100, height=30)
        self.search_button.place(x=500, y=425, width=100, height=30)
        self.logout_button.place(x=500, y=460, width=100, height=30)

        self.display_books(self.app.books_df)

    def display_books(self, books_df):
        self.books_display.config(state=tk.NORMAL)
        self.books_display.delete(1.0, tk.END)

        if books_df.empty:
            self.books_display.insert(tk.END, "No books found.\n")
        else:
            self.books_display.config(font=("Courier", 10))

            header = f"{'ID':<5} {'Title':<30} {'Author':<25} {'Price':<10} {'Quantity':<10} {'Genre':<15}\n"
            self.books_display.insert(tk.END, header)
            self.books_display.insert(tk.END, "-" * (len(header) + 4) + "\n")

            for _, row in books_df.iterrows():
                formatted_row = (
                    f"{row['book_id']:<5} "
                    f"{row['title'][:30]:<30} "
                    f"{row['author'][:25]:<25} "
                    f"{row['price']:<10.2f} "
                    f"{row['quantity']:<10} "
                    f"{row['genre'][:15]:<15}\n"
                )
                self.books_display.insert(tk.END, formatted_row)

        self.books_display.config(state=tk.DISABLED)

    def handle_logout(self):
        from frontend.login_page import Login_Gui
        self.app.logout()
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
            self.update_display("No books found matching your search")
        else:
            self.display_books(results)

    def add_to_cart(self):
        title = self.get_selected_book_title()
        if not title:
            messagebox.showwarning("Warning", "Please enter a valid book title")
            return
        title = title.strip().lower()
        result = self.user.add_to_cart(title, 1)
        messagebox.showinfo("Cart Update", result)
        self.display_books(self.app.books_df)

    def get_selected_book_title(self):
        return self.search_entry.get().strip()
    
    def remove_from_cart(self):
        title = self.get_selected_book_title()
        result = self.user.remove_from_cart(title)
        messagebox.showinfo("Cart Update", result)
        self.display_books(self.app.books_df)
        
    def update_display(self, text):
        self.books_display.config(state=NORMAL)
        self.books_display.delete(1.0, END)
        self.books_display.insert(END, text)
        self.books_display.config(state=DISABLED)

    def checkout(self):
        checkout_summary = self.user.checkout()
        if "Your cart is empty" in checkout_summary:
            messagebox.showwarning("Checkout", checkout_summary)
        else:
            self.update_display(checkout_summary)
            messagebox.showinfo("Checkout Complete", "Thank you for your purchase!")