from tkinter import *
from tkinter import messagebox
import json

class Login_Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Login / Signup")
        self.config(padx=70, pady=70, bg="#2e2e2e")

        self.canvas = Canvas(width = 360, height = 360, bg="#2e2e2e", highlightthickness=0)
        self.logo = PhotoImage(file = "Assets/logo.png") 
        self.canvas.create_image(180, 180, image=self.logo)
        self.canvas.grid(column=1, row=0)

        self.username_entry = Entry(width=30, bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.username_entry.focus()
        self.username_entry.grid(column=1, row=2)
        self.password_entry = Entry(width=30, show="*", bg="#3c3c3c", fg="white", insertbackground="white", font=("Helvetica", 12))
        self.password_entry.grid(column=1, row=4)

        self.canvas = Canvas(width = 360, height = 360, bg = "#2e2e2e", highlightthickness = 0)
        self.logo = PhotoImage(file = "Assets/logo.png")
        self.canvas.create_image(180, 160, image = self.logo)
        self.canvas.grid(column = 1, row = 0)

        self.username_label = Label(text = "Username:", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.username_label.grid(column = 1, row = 1)
        self.password_label = Label(text = "Password:", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.password_label.grid(column = 1, row = 3)

        self.login_logo = PhotoImage(file = "Assets/log-in.png")
        self.login_button = Button(text = "Login", width = 15, bg = "#28a745", fg = "white", highlightthickness = 0, command = self.details_check)
        self.login_button.grid(column = 1, row = 5, pady = 10)
        self.signup_logo = PhotoImage(file = "Assets/sign-up.png")
        self.signup_button = Button(text = "Signup", width = 15, bg = "#007bff", fg = "white", highlightthickness = 0, command = self.save)
        self.signup_button.grid(column = 1, row = 6, pady = 10)


    def save(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        new_data = {username:
            {
                "password" : self.encode(password),
            }
        }

        if username == "" or password == "":
            messagebox.showwarning(title = "Oops", message = "Please don't leave any fields empty!")
    
def login_action():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def signup_action():
    messagebox.showinfo("Signup", "Signup functionality not implemented yet.")

root = tk.Tk()
root.title("Login / Signup")
root.geometry("400x600")

root.configure(bg='#2c2c2c')

logo_image_path = "D:\Projects\Library_Management_System\Assets\logo.png"
logo_img = Image.open(logo_image_path).resize((150, 150))
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(root, image=logo_photo, bg='#2c2c2c')
logo_label.pack(pady=40)

def loggedin_window(self):
    if self.username_entry.get()[:5] == "admin":
        from adminGUI import Admin_Gui 
        self.destroy()
        admin_window = Admin_Gui()
    else:
        from userGUI import User_Gui
        self.destroy()
        user_window = User_Gui()
