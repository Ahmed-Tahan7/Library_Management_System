from tkinter import *
from tkinter import ttk
from loginGUI import Login_Gui
class User_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System / User")
        self.config(padx=150, pady=130, bg="#2e2e2e")
        
        self.screen = Text(state = DISABLED , width = 50, height = 20, bg = "#3c3c3c", fg = "white", insertbackground = "white", font = ("Helvetica", 12))
        self.screen.grid(column = 1, row = 0)

        self.search = ttk.Combobox()
        self.search.place(x=40, y=380, width=300, height=30)

        self.add_button = Button(text = "Add Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.inventory_button = Button(text = "View Cart", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.remove_button = Button(text = "Remove Book", bg = "#2e2e2e", fg = "white", highlightthickness = 0)
        self.logout_button = Button(text = "Logout", bg = "#2e2e2e", fg = "white", highlightthickness = 0, command = self.logout)
        self.filter = ttk.Combobox()
        self.filter.set("Filter By:")
        self.filter.config(state = "readonly")
        self.filtered = self.filter.get()

        self.add_button.place(x=110, y=425, width=100, height=30)
        self.remove_button.place(x=260, y=425, width=100, height=30)
        self.inventory_button.place(x=110, y=460, width=100, height=30)
        self.logout_button.place(x=260, y=460, width=100, height=30)
        self.filter.place(x=350, y=380, width=100, height=30)
    
    def logout(self):
        self.destroy()
        app = Login_Gui()
