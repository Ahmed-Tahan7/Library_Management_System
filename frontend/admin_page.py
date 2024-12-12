from tkinter import *
from tkinter import messagebox
import tkinter as tk
from backend.library_system import LibrarySystem
from backend.admin import Admin

class Admin_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System / Admin")
        self.app = LibrarySystem()
        self.admin = Admin(self.app.current_user, self.app)
        self.config(padx=110, pady=180, bg="#2e2e2e")

        self.title_label = Label(text="Welcome to The Whispering Pages Bookstore - Admin", bg="#2e2e2e", fg="white", highlightthickness=0, font=("Helvetica", 18))
        self.title_label.grid(column=1, row=0)

        self.books_display = Text(state=DISABLED, width=105, height=20, bg="#3c3c3c", fg="white", insertbackground="white", font=("Courier", 10))
        self.books_display.grid(column=1, row=1)

        self.search_entry = Entry(self, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.search_entry.place(x=200, y=380, width=300, height=30)

        self.add_button = Button(text="Add Book", bg="#28a745", fg="white", highlightthickness=0, command=self.add_book)
        self.inventory_button = Button(text="Inventory", bg="#6c757d", fg="white", highlightthickness=0, command=self.view_inventory)
        self.remove_button = Button(text="Remove Book", bg="#dc3545", fg="white", highlightthickness=0, command=self.remove_book)
        self.search_button = Button(text="Search", bg="#007bff", fg="white", highlightthickness=0, command=self.search_books)
        self.logout_button = Button(text="Logout", bg="#a71e2a", fg="white", highlightthickness=0, command=self.handle_logout)

        self.add_button.place(x=250, y=425, width=100, height=30)
        self.remove_button.place(x=450, y=425, width=100, height=30)
        self.inventory_button.place(x=250, y=460, width=100, height=30)
        self.search_button.place(x=520, y=380, width=100, height=30)
        self.logout_button.place(x=450, y=460, width=100, height=30)

        self.display_books(self.app.books_df)

    def display_books(self, books_df):

        self.books_display.config(state=NORMAL)
        self.books_display.delete(1.0, END)

        if books_df.empty:
            self.books_display.insert(END, "No books found.\n")
        else:
            self.books_display.config(font=("Courier", 10))

            header = f"{'ID':<5} {'Title':<30} {'Author':<25} {'Price':<10} {'Quantity':<10} {'Genre':<15}\n"
            self.books_display.insert(END, header)
            self.books_display.insert(END, "-" * (len(header) + 4) + "\n")

            for _, row in books_df.iterrows():
                formatted_row = (
                    f"{row['book_id']:<5} "
                    f"{row['title'][:30]:<30} "
                    f"{row['author'][:25]:<25} "
                    f"{row['price']:<10.2f} "
                    f"{row['quantity']:<10} "
                    f"{row['genre'][:15]:<15}\n"
                )
                self.books_display.insert(END, formatted_row)

        self.books_display.config(state=DISABLED)

    def handle_logout(self):
        from frontend.login_page import Login_Gui
        self.app.logout()
        self.destroy()
        Login_Gui()

    def search_books(self):
        search_term = self.search_entry.get().strip()
        results = self.app.search_books(search_term, filter_option=None)
        if results.empty:
            self.update_display("No books found matching your search.")
        else:
            self.display_books(results)

    def view_inventory(self):
        inventory_contents = self.admin.view_books()
        self.display_books(inventory_contents)

    def update_display(self, text):
        self.books_display.config(state=NORMAL)
        self.books_display.delete(1.0, END)
        self.books_display.insert(END, text)
        self.books_display.config(state=DISABLED)

    def get_selected_book_id(self):
        try:
            return int(self.search_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid Book ID.")
            return None

    def remove_book(self):
        dialog = tk.Toplevel(self)
        dialog.title("Remove Book")
        dialog.geometry("400x150")
        dialog.config(padx=20, pady=20, bg="#2e2e2e")

        label = tk.Label(dialog, text="Enter Book Title:", bg="#2e2e2e", fg="white", font=("Helvetica", 10))
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        book_title_entry = tk.Entry(dialog, bg="#3c3c3c", fg="white", font=("Helvetica", 10), width=30)
        book_title_entry.grid(row=0, column=1, padx=5, pady=5)

        def submit():
            title = book_title_entry.get().strip()
            if not title:
                messagebox.showerror("Input Error", "Book Title cannot be empty.")
                return
            try:
                result = self.admin.remove_book(title)  # Call Admin's remove_book method
                messagebox.showinfo("Success", result)
                self.view_inventory()  # Refresh the book display
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            dialog.destroy()

        submit_button = tk.Button(dialog, text="Submit", bg="#28a745", fg="white", command=submit)
        submit_button.grid(row=1, column=1, pady=10)

        dialog.transient(self)
        dialog.grab_set()
        self.wait_window(dialog)
        
    def book_details(self):
        details = {}
        dialog = tk.Toplevel(self)
        dialog.title("Enter Book Details")
        dialog.geometry("400x300")
        dialog.config(padx=15, pady=15, bg="#2e2e2e")

        fields = ["Book ID", "Title", "Author", "Price", "Quantity", "Genre"]
        entries = {}

        for idx, field in enumerate(fields):
            label = tk.Label(dialog, text=field, bg="#2e2e2e", fg="white", font=("Helvetica", 10))
            label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(dialog, bg="#3c3c3c", fg="white", font=("Helvetica", 10), width=30)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            entries[field] = entry

        def submit():
            try:
                for field in fields:
                    value = entries[field].get().strip()
                    if not value:
                        raise ValueError(f"{field} cannot be empty.")
                    
                    if field == "Price":
                        value = float(value)
                    elif field == "Quantity":
                        value = int(value)
                    
                    details[field.lower().replace(" ", "_")] = value
                
                dialog.destroy()
            except ValueError as e:
                messagebox.showerror("Input Error", str(e))

        submit_button = tk.Button(dialog, text="Submit", bg="#28a745", fg="white", command=submit)
        submit_button.grid(row=len(fields), column=1, pady=10)

        dialog.transient(self)
        dialog.grab_set()
        self.wait_window(dialog)

        return details


    def add_book(self):
        book_data = self.book_details()
        if book_data:
            result = self.admin.add_book(book_data)
            self.update_display(result)
