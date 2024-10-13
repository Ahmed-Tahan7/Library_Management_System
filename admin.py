from person import Person
from book import Book
from libraryManager import Library_Manager

class Admin(Person):
    def __init__(self, name, user_id, password):
        super().__init__(name, user_id, password)

    def add_book(self, library_manager, book):
        if isinstance(library_manager, Library_Manager) and isinstance(book, Book):
            library_manager.add_book(book)
            print(f"Book '{book.title}' added to the stock.")
        else:
            raise TypeError("Invalid Input!!")

    def remove_book(self, library_manager, book_id):
        if isinstance(library_manager, Library_Manager):
            library_manager.remove_book(book_id)
        else:
            raise TypeError("Invalid Input!!")
