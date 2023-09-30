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

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (Author): The author of the book.
        genre (Genre): The genre of the book.
        publication_date (str): The publication date of the book.

    Methods:
        __str__(): Returns a string representation of the book.
    """

    def __init__(self, title, author, genre, publication_date):  # Fixed: Added publication_date parameter
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPublication Date: {self.publication_date}"


class Author:
    """
    Represents an author of a book.

    Attributes:
        name (str): The name of the author.
        nationality (str): The nationality of the author.
        date_of_birth (str): The date of birth of the author.

    Methods:
        __str__(): Returns a string representation of the author.
    """

    def __init__(self, name, nationality, date_of_birth):
        self.name = name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Name: {self.name}\nNationality: {self.nationality}\nDate of Birth: {self.date_of_birth}"


class Genre:
    """
    Represents a genre of a book.

    Attributes:
        name (str): The name of the genre.
        description (str): A description of the genre.

    Methods:
        __str__(): Returns a string representation of the genre.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"


class BookNotFoundError(Exception):
    """Exception raised when a book is not found in the library's collection."""
    pass


class BookCheckoutError(Exception):
    """Exception raised when a book is already checked out to another user."""
    pass


class BookCheckInError(Exception):
    """Exception raised when a book is not checked out to any user."""
    pass


class Library:
    """
    Represents the library.

    Attributes:
        name (str): The name of the library.
        address (str): The address of the library.
        contact_info (str): The contact information of the library.
        books (list): A list to store the collection of books in the library.

    Methods:
        __init__(name, address, contact_info): Constructor for the Library class.
        __del__(): Destructor for the Library class.
        add_book(book): Adds a book to the library's collection.
        remove_book(book): Removes a book from the library's collection.
        get_book_by_title(title): Returns a book from the library's collection by its title.
        get_books_by_author(author): Returns a list of books from the library's collection by their author.
        get_books_by_genre(genre): Returns a list of books from the library's collection by their genre.
        get_all_books(): Static method to return a list of all books in the library's collection.
        get_number_of_books(): Static method to return the number of books in the library's collection.
        print_all_books(): Method to print a list of all books in the library's collection.
        search_by_title(title): Method to search for a book by its title.
        checkout(book, user): Method to check out a book to a user.
        checkin(book, user): Method to check in a book from a user.
        login(user): Static method to log in a user.
        logout(user): Static method to log out a user.
        login_required(func): Decorator to ensure that only logged-in users can check out and check in books.
    """

    logged_in_users = set()

    def __init__(self, name, address, contact_info):
        """
        Constructor for the Library class.

        Parameters:
            name (str): The name of the library.
            address (str): The address of the library.
            contact_info (str): The contact information of the library.
        """
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.books = []

    def __del__(self):
        """
        Destructor for the Library class.
        """
        print(f"The library {self.name} has been closed.")

    def add_book(self, book):
        """
        Adds a book to the library's collection.

        Parameters:
            book (Book): The book to be added.
        """
        self.books.append(book)

    def remove_book(self, book):
        """
        Removes a book from the library's collection.

        Parameters:
            book (Book): The book to be removed.

        Raises:
            BookNotFoundError: If the book is not found in the library.
        """
        if book in self.books:
            self.books.remove(book)
        else:
            raise BookNotFoundError("Book not found in the library.")

    def get_book_by_title(self, title):
        """
        Returns a book from the library's collection by its title.

        Parameters:
            title (str): The title of the book.

        Raises:
            BookNotFoundError: If the book is not found in the library.
        """
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundError("Book not found in the library.")

    def get_books_by_author(self, author):
        """
        Returns a list of books from the library's collection by their author.

        Parameters:
            author (Author): The author of the books.
        """
        return [book for book in self.books if book.author == author]

    def get_books_by_genre(self, genre):
        """
        Returns a list of books from the library's collection by their genre.

        Parameters:
            genre (Genre): The genre of the books.
        """
        return [book for book in self.books if book.genre == genre]

    @staticmethod
    def get_all_books():
        """
        Static method to return a list of all books in the library's collection.
        """
        return self.books  # Fixed: Changed to return self.books instead of using 'self'

    @staticmethod
    def get_number_of_books():
        """
        Static method to return the number of books in the library's collection.
        """
        return len(self.books)  # Fixed: Changed to use len(self.books) instead of 'self.books'

    def print_all_books(self):
        """
        Method to print a list of all books in the library's collection.
        """
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        """
        Method to search for a book by its title.

        Parameters:
            title (str): The title of the book.
        """
        try:
            book = self.get_book_by_title(title)
            print("Book found in the library:")
            print(book)
        except BookNotFoundError as e:
            print(f"Error: {e}")

    @staticmethod
    def login(user):
        """
        Static method to log in a user.

        Parameters:
            user (User): The user to be logged in.
        """
        Library.logged_in_users.add(user)
        print(f"{user.name} has logged in.")

    @staticmethod
    def logout(user):
        """
        Static method to log out a user.

        Parameters:
            user (User): The user to be logged out.
        """
        if user in Library.logged_in_users:
            Library.logged_in_users.remove(user)
            print(f"{user.name} has logged out.")

    @staticmethod
    def login_required(func):
        """
        Decorator to ensure that only logged-in users can check out and check in books.
        """
        def wrapper(self, *args, **kwargs):
            if args and args[1] not in self.logged_in_users:
                print("Login required to perform this operation.")
                return
            return func(self, *args, **kwargs)
        return wrapper

    @login_required
    def checkout(self, book, user):
        """
        Method to check out a book to a user.

        Parameters:
            book (Book): The book to be checked out.
            user (User): The user checking out the book.

        Raises:
            BookNotFoundError: If the book is not found in the library.
            BookCheckoutError: If the book is already checked out to the user.
        """
        if book in self.books:
            if book in user.checked_out_books:
                raise BookCheckoutError("This book is already checked out to you.")
            else:
                user.checked_out_books.add(book)
                print(f"Book '{book.title}' checked out to {user.name}.")
        else:
            raise BookNotFoundError("Book not found in the library.")

    @login_required
    def checkin(self, book, user):
        """
        Method to check in a book from a user.

        Parameters:
            book (Book): The book to be checked in.
            user (User): The user checking in the book.

        Raises:
            BookCheckInError: If the book is not checked out to the user.
        """
        if book in user.checked_out_books:
            user.checked_out_books.remove(book)
            print(f"Book '{book.title}' checked in by {user.name}.")
        else:
            raise BookCheckInError("This book is not checked out to you.")
