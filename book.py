class Book:
    
    def __init__(self, title, author, genre, publication_year, price, availability=True, rental_price=None, rental_duration=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.price = price
        self.availability = availability
        self.rental_price = rental_price
        self.rental_duration = rental_duration

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Publication Year: {self.publication_year}, Price: {self.price}"

    def update_availability(self, status):
        self.availability = status

    def calculate_rental_cost(self):
        if self.rental_price is not None and self.rental_duration is not None:
            return self.rental_price * self.rental_duration

    def is_available(self):
        return self.availability
