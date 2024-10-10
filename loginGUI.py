from userGUI import *
from adminGUI import *
from tkinter import *
from tkinter import messagebox
from adminGUI import *
from userGUI import *
import json
import string

class Login_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login / Signup")
        self.config(padx=70, pady=65, bg="#2e2e2e")

        self.canvas = Canvas(width=360, height=360, bg="#2e2e2e", highlightthickness=0)
        self.logo = PhotoImage(file="Assets/logo.png") 
        self.canvas.create_image(180, 180, image=self.logo)
        self.canvas.grid(column=1, row=0)

        self.username_entry = Entry(width=30, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.username_entry.focus()
        self.username_entry.grid(column=1, row=2, pady=10)
        self.password_entry = Entry(width=30, show="*", bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.password_entry.grid(column=1, row=4, pady=10)

        self.username_label = Label(text="Username:", bg="#2e2e2e", fg="white", font=("Helvetica", 12))
        self.username_label.grid(column=1, row=1, pady=5)
        self.password_label = Label(text="Password:", bg="#2e2e2e", fg="white", font=("Helvetica", 12))
        self.password_label.grid(column=1, row=3, pady=5)

        self.login_button = Button(text="Login", bg="#4CAF50", fg="white", font=("Helvetica", 12), command=self.details_check, width=15)
        self.login_button.grid(column=1, row=5, pady=10)

        self.signup_button = Button(text="Signup", bg="#2196F3", fg="white", font=("Helvetica", 12), command=self.save, width=15)
        self.signup_button.grid(column=1, row=6, pady=10)

    def save(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        new_data = {username: {"password": self.encode(password)}}

        if username == "" or password == "":
            messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title="Signup", message=f"These are the details entered:\nUsername: {username}\nPassword: {password}\nIs it okay to save?")
            if is_ok:
                try:
                    with open("Login_Details.json", "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("Login_Details.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    if username in data:
                        messagebox.showwarning(title="Oops", message="Username already exists")
                    else:
                        data.update(new_data)
                        with open("Login_Details.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)

                finally:
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                    self.username_entry.focus()

    def details_check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("Login_Details.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found")
        else:
            if username in data and self.encode(password) == data[username]["password"]:
                self.loggedin_window()
            elif username in data and self.encode(password) != data[username]["password"]:
                messagebox.showwarning(title="Error", message="Password or username is incorrect")
            else:
                messagebox.showwarning(title="Error", message="No details were found")

    def encode(self, password):
        alphabet_lower = string.ascii_lowercase
        alphabet_upper = string.ascii_uppercase  
        shift = 5
        end_text = ""
        for char in password:
            if char in alphabet_lower:
                position = alphabet_lower.index(char)
                new_position = (position + shift) % 26
                end_text += alphabet_lower[new_position]
            elif char in alphabet_upper:
                position = alphabet_upper.index(char)
                new_position = (position + shift) % 26
                end_text += alphabet_upper[new_position]
            else:
                end_text += char
        return end_text

    def loggedin_window(self):
        if self.username_entry.get().startswith("admin"):
            self.destroy() 
            admin_window = Admin_Gui() 
        else:
            self.destroy()  
            user_window = User_Gui()  



