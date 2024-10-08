from tkinter import *
from tkinter import messagebox
class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Managment System")
        self.config(padx = 70, pady = 65, bg = "light gray")

        self.username_entry = Entry(width = 40)
        self.username_entry.focus()
        self.username_entry.grid(column = 1, row = 2)
        self.password_entry = Entry(width = 40, show = "*")
        self.password_entry.grid(column = 1, row = 4)

        self.canvas = Canvas(width = 360, height = 360, bg = "light gray", highlightthickness = 0)
        self.logo = PhotoImage(file = "Assets/file.png")
        self.canvas.create_image(165, 160, image = self.logo)
        self.canvas.grid(column = 1, row = 0)


        self.username_label = Label(text = "Username:", bg = "light gray", highlightthickness = 0)
        self.username_label.grid(column = 1, row = 1)
        self.password_label = Label(text = "Password:", bg = "light gray", highlightthickness = 0)
        self.password_label.grid(column = 1, row = 3)


        self.login_logo = PhotoImage(file = "Assets/log-in.png")
        self.login_button = Button(image = self.login_logo, bd = 0, bg = "light gray", highlightthickness = 0)
        self.login_button.grid(column = 0, row = 5)
        self.signup_logo = PhotoImage(file = "Assets/sign-up.png")
        self.signup_button = Button(image = self.signup_logo, bd = 0, bg = "light gray", highlightthickness = 0)
        self.signup_button.grid(column = 2, row = 5)