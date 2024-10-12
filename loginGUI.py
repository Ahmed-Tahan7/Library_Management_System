import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

def load_credentials():
    with open('credentials.json', 'r') as f:
        return json.load(f)
    
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

username_label = tk.Label(root, text="Username", font=('Arial', 12), fg='white', bg='#2c2c2c')
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=('Arial', 12), width=30, bd=2, relief='flat')
username_entry.pack()

password_label = tk.Label(root, text="Password", font=('Arial', 12), fg='white', bg='#2c2c2c')
password_label.pack(pady=10)
password_entry = tk.Entry(root, font=('Arial', 12), width=30, bd=2, relief='flat', show='*')
password_entry.pack()

login_button = tk.Button(root, text="Login", font=('Arial', 12), width=15, bg='#28a745', fg='white', command=login_action)
login_button.pack(pady=20)

signup_button = tk.Button(root, text="Signup", font=('Arial', 12), width=15, bg='#007bff', fg='white', command=signup_action)
signup_button.pack(pady=10)

root.mainloop()
