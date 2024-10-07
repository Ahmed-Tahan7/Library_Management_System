from person import Person
from book import Book
class User(Person):

    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.rented_books = []

    def buy_book(self, book):
        if book.availability:
            print(f"{self.name} has bought '{book.title}' for ${book.price}.")
            book.availability = False
        else:
            return f"{book.title} is not available for purchase"

    def rent_book(self, book):
        if book.availability:
            self.rent_book.append(book)
            book.availability = False
            return f"{self.name} has rented {book.title}"
        else:
            return f"{book.title} is not available"
        
    def get_rented_books(self):
        if self.rented_books:
            return [book.get_details() for book in self.rented_books]
        return "No rented books."
    

    def return_book(self, book):
        if book in self.rented_books:
            self.rented_books.remove(book)
            book.availability = True
            return f"{self.name} has returned {book.title}"
        else:
            return f"{self.name} does not have {book.title} rented"
