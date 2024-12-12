from tkinter import *
from tkinter import messagebox
from backend.library_system import LibrarySystem

class Login_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.app = LibrarySystem()

        self.title("Login / Signup")
        self.config(padx=70, pady=70, bg="#2e2e2e")

        self.canvas = Canvas(width = 360, height = 360, bg="#2e2e2e", highlightthickness=0)
        self.logo = PhotoImage(file = r"Assets\\logo.png") 
        self.canvas.create_image(180, 180, image=self.logo)
        self.canvas.grid(column=1, row=1)

        self.username_entry = Entry(width=30, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.username_entry.focus()
        self.username_entry.grid(column=1, row=3)
        self.password_entry = Entry(width=30, show="*", bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.password_entry.grid(column=1, row=5)

        self.title_label = Label(text = "The Whispering Pages Bookstore", bg = "#2e2e2e", fg = "white", highlightthickness = 0, font=("Helvetica", 18))
        self.title_label.grid(column = 1, row = 0)
        self.username_label = Label(text = "Username:", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.username_label.grid(column = 1, row = 2)
        self.password_label = Label(text = "Password:", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.password_label.grid(column = 1, row = 4)
        self.empty_label = Label(text = "", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.empty_label.grid(column = 1, row = 6)

        self.login_button = Button(text = "Login", height=2, width = 20, bg = "#28a745", fg = "white", highlightthickness = 0, command = self.handle_login)
        self.login_button.grid(column = 1, row = 7, pady = 10)
        self.signup_button = Button(text = "Signup", height=2, width = 20, bg = "#007bff", fg = "white", highlightthickness = 0, command=self.handel_signup)
        self.signup_button.grid(column = 1, row = 8, pady = 10)
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter username and password")
        else:
            status = self.app.login(username, password)
            if status:
                self.destroy()
                if self.app.current_user.role == "admin":
                    from frontend.admin_page import Admin_Gui
                    self.app = Admin_Gui()
                else:
                    from frontend.user_page import User_Gui
                    self.app = User_Gui()
            else:
                messagebox.showerror("Error", "Invalid username or password")

    def handel_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter username and password")
        else:
            success = self.app.add_new_user(username, password)
            messagebox.showinfo("Status", success)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.username_entry.focus()
