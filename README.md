# The Whispering Pages Bookstore Management System

## Project Overview
The Whispering Pages Bookstore Management System is a Python-based application designed to streamline bookstore operations for both administrators and users. With an intuitive GUI built using Tkinter, the system provides a range of features for managing inventory, user authentication, and book purchases.

---

## Features

### Admin Features:
- **Add Books:** Add new books to the inventory with relevant details (ID, title, author, price, quantity, genre).
- **Remove Books:** Remove books from the inventory by title.
- **View Inventory:** Display all books in the inventory.
- **Search Books:** Search books by title, author, or genre.

### User Features:
- **Search Books:** Search for books by title, author, or genre.
- **Add to Cart:** Add desired books to the cart.
- **View Cart:** Review the books added to the cart.
- **Remove from Cart:** Remove specific books from the cart.
- **Checkout:** Purchase all items in the cart.

---

## Project Structure
```
library_management_system/
├── backend/
│   ├── library_system.py       # Core logic and system backend
│   ├── admin.py                # Admin-specific functionality
│   ├── user.py                 # User-specific functionality
│   ├── person.py               # Base class for users and admins
│   ├── cipher.py               # Handles password encryption and decryption
├── frontend/
│   ├── login_page.py           # Login and signup GUI
│   ├── admin_page.py           # Admin-specific GUI
│   ├── user_page.py            # User-specific GUI
├── data/
│   ├── books.csv               # Book inventory
│   ├── loginDetails.json       # User credentials
├── Assets/
│   ├── logo.png                # Application logo
├── main.py                     # Application entry point
```

---

## Setup and Installation

### Prerequisites
- Python 3.8 or above.
- Required libraries: Install dependencies via `pip install -r requirements.txt`.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed-Tahan7/library-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```
3. Run the main application:
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the application by running `main.py`.
2. **Login or Signup:**
   - Use the login screen to authenticate as an admin or user.
3. **Admin Operations:**
   - Add, remove, search, or view books using the Admin GUI.
4. **User Operations:**
   - Search for books, add to the cart, view cart, or proceed to checkout using the User GUI.

---

## Technical Details
- **Programming Language:** Python
- **Frameworks and Libraries:**
  - GUI: Tkinter
  - Data Handling: Pandas
  - Encryption: Base64 (Custom Cipher Class)
- **Data Storage:**
  - User credentials stored in `loginDetails.json`.
  - Book inventory managed in `books.csv`.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

---

## Acknowledgments
This project was developed as a learning exercise for Python application development, incorporating object-oriented programming (OOP) and design patterns.

---

## Contact
For inquiries or feedback, please contact:
- **Developer Name:** Ahmed Tahan || Abdelrahman Gawad
- **Email:** ahmed.tahan71@gmail.com || 

