from tkinter import *
from tkinter import messagebox
from adminGUI import *
from userGUI import *
from encryption import *
import json
class Login_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login / Sginup")
        self.config(padx = 70, pady = 65, bg = "light gray")

        self.username_entry = Entry(width = 40)
        self.username_entry.focus()
        self.username_entry.grid(column = 1, row = 2)
        self.password_entry = Entry(width = 40, show = "*")
        self.password_entry.grid(column = 1, row = 4)

        self.canvas = Canvas(width = 360, height = 360, bg = "light gray", highlightthickness = 0)
        self.logo = PhotoImage(file = "Assets/logo.png")
        self.canvas.create_image(180, 160, image = self.logo)
        self.canvas.grid(column = 1, row = 0)


        self.username_label = Label(text = "Username:", bg = "light gray", highlightthickness = 0)
        self.username_label.grid(column = 1, row = 1)
        self.password_label = Label(text = "Password:", bg = "light gray", highlightthickness = 0)
        self.password_label.grid(column = 1, row = 3)


        self.login_logo = PhotoImage(file = "Assets/log-in.png")
        self.login_button = Button(image = self.login_logo, bd = 0, bg = "light gray", highlightthickness = 0, command = self.details_check)
        self.login_button.grid(column = 0, row = 5)
        self.signup_logo = PhotoImage(file = "Assets/sign-up.png")
        self.signup_button = Button(image = self.signup_logo, bd = 0, bg = "light gray", highlightthickness = 0, command = self.save)
        self.signup_button.grid(column = 2, row = 5)

    def save(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        new_data = {username:
        {
            "password" : password,
        }
    }

        if username == "" or password == "":
            messagebox.showwarning(title = "Oops", message = "Please don't leave any fields empty!")
    
        else:
            is_ok = messagebox.askokcancel(title = f"Signup", message = f"These are the details entered:\nusername: {username}"
                                    f"\nPassword: {password} \nIs it okay to save?")
            if is_ok:
                try:
                    with open("Login Details.json", "r") as data_file:
                        data = json.load(data_file)
            
                except FileNotFoundError:
                    with open("Login Details.json", "w") as data_file:
                        json.dump(new_data, data_file, indent = 4)
            
                else:
                    data.update(new_data)
                    with open("Login Details.json","w") as data_file:
                        json.dump(data, data_file, indent = 4)
            
                finally:
                    self.username_entry.delete(0, END)
                    self.username_entry.focus()
                    self.password_entry.delete(0, END)

    def details_check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            with open("Login Details.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title = "Error", message = "No Data File Found")
        else:
            if username in data and password == data[username]["password"]:
                self.loggedin_window()
            elif username in data and password != data[username]["password"]:
                messagebox.showwarning(title = "Error", message = "Password or username is incorrect")
            else:
                messagebox.showwarning(title = "Error", message = "No details where found")


    def loggedin_window(self):
        if self.username_entry.get()[:5] == "admin": 
            self.destroy()
            admin_window = Admin_Gui()
        else:
            self.destroy()
            user_window = User_Gui()