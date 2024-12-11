class Person:
    """ Represents common attributes and methods shared by Admin and User """

    def __init__(self, username, role, library_system):
        self.username = username
        self.role = role
        self.library_system = library_system

    def view_books(self):
        return self.library_system.books_df

    def logout(self):
        self.library_system.logout()
        print(f"{self.username} has been logged out")

    def __str__(self):
        return f"Username: {self.username}, Role: {self.role}"