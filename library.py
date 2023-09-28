"""
Library Management System in Python

This code implements a Python class hierarchy to model a library system. The system includes the following classes:

* Book: This class represents a book in the library. It has attributes such as title, author, genre, and publication date.
* Author: This class represents an author of a book. It has attributes such as name, nationality, and date of birth.
* Genre: This class represents a genre of a book. It has attributes such as name and description.
* Library: This class represents the library itself. It has attributes such as name, address, and contact information. It also has a collection of books.

The Library class has the following methods:

* add_book(book): This method adds a book to the library's collection.
* remove_book(book): This method removes a book from the library's collection.
* get_book_by_title(title): This method returns a book from the library's collection by its title.
* get_books_by_author(author): This method returns a list of books from the library's collection by their author.
* get_books_by_genre(genre): This method returns a list of books from the library's collection by their genre.

The Library class also has the following static methods:

* get_all_books(): This method returns a list of all books in the library's collection.
* get_number_of_books(): This method returns the number of books in the library's collection.

The Library class also has a constructor and a destructor.

The Book, Author, and Genre classes also have constructors and destructors.

The Book, Author, and Genre classes also have methods to print their information.

The Library class also has a method to print a list of all books in its collection.

The Library class also has a method to search for a book by its title.

The Library class also has a method to check out a book to a user.

The Library class also has a method to check in a book from a user.

The Library class also handles exceptions such as:

* BookNotFoundError: This exception is raised if a book is not found in the library's collection.
* BookCheckoutError: This exception is raised if a book is already checked out to another user.
* BookCheckInError: This exception is raised if a book is not checked out to any user.

The Library class also has a decorator to decorate its checkout() and checkin() methods to ensure that only logged-in users can check out and check in books.
"""

import copy

# User-defined exceptions
class BookNotFoundError(Exception):
    pass

class BookCheckoutError(Exception):
    pass

class BookCheckInError(Exception):
    pass

# Base class for Author
class Author:
    def __init__(self, name, nationality, dob):
        self.name = name
        self.nationality = nationality
        self.dob = dob

    def __str__(self):
        return f"{self.name} ({self.nationality}, {self.dob})"

# Base class for Genre
class Genre:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

# Base class for Book
class Book:
    def __init__(self, title, author, genre, pub_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pub_date}\nGenre: {self.genre}"

    def __repr__(self):
        return f"Book('{self.title}', {repr(self.author)}, {repr(self.genre)}, '{self.pub_date}')"

    def clone(self):
        # Implementing object cloning using copy module
        return copy.deepcopy(self)

# Library class
class Library:
    # Static attribute to store all books
    all_books = []

    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        # Collection of books using a list
        self.books = []

    def __del__(self):
        print(f"The library {self.name} is closing.")

    def add_book(self, book):
        self.books.append(book)
        # Adding the book to the static attribute for all books
        Library.all_books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            Library.all_books.remove(book)
        else:
            raise BookNotFoundError("Book not found in the library.")

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundError(f"Book with title '{title}' not found in the library.")

    def get_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def get_books_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

    @staticmethod
    def get_all_books():
        return Library.all_books

    @staticmethod
    def get_number_of_books():
        return len(Library.all_books)

    def print_books(self):
        for book in self.books:
            print(book)

    def search_book_by_title(self, title):
        try:
            book = self.get_book_by_title(title)
            print(f"Book found:\n{book}")
        except BookNotFoundError as e:
            print(e)

    def checkout_decorator(func):
        # Decorator to check if the user is logged in before checking out or checking in a book
        def wrapper(self, book, user):
            if user.is_logged_in:
                return func(self, book, user)
            else:
                print("User not logged in. Please log in to check out or check in a book.")
        return wrapper

    @checkout_decorator
    def checkout(self, book, user):
        if book in self.books:
            if book not in user.checked_out_books:
                user.checked_out_books.append(book)
                self.books.remove(book)
                print(f"{user.name} checked out {book.title}.")
            else:
                raise BookCheckoutError(f"{book.title} is already checked out to {user.name}.")
        else:
            raise BookNotFoundError("Book not found in the library.")

    @checkout_decorator
    def checkin(self, book, user):
        if book in user.checked_out_books:
            user.checked_out_books.remove(book)
            self.books.append(book)
            print(f"{user.name} checked in {book.title}.")
        else:
            raise BookCheckInError(f"{user.name} does not have {book.title} checked out.")

# User class to represent library users
class User:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.name} is now logged in.")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.name} is now logged out.")

# Sample usage
if __name__ == "__main__":
    # Creating instances of Author and Genre
    author1 = Author("John Doe", "American", "01-01-1970")
    genre1 = Genre("Mystery", "A mysterious genre")

    # Creating instances of Book
    book1 = Book("The Mystery Book", author1, genre1, "01-01-2000")

    # Creating an instance of Library
    library1 = Library("City Library", "123 Main St", "555-1234")

    # Adding the book to the library
    library1.add_book(book1)

    # Creating a user
    user1 = User("Alice")

    # Logging in the user
    user1.login()

    # Checking out a book
    library1.checkout(book1, user1)

    # Printing all books in the library
    library1.print_books()

    # Searching for a book by title
    library1.search_book_by_title("The Mystery Book")

    # Checking in a book
    library1.checkin(book1, user1)

    # Logging out the user
    user1.logout()
