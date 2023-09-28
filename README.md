# oops-exceptions

This is the best possible OOPS +EXCEPTION HANDLING example you can find to solidify your understanding of the language and the topic,
it has the following features:


Design a Python class hierarchy to model a library system. The system should include the following classes:

Book: This class should represent a book in the library. It should have attributes such as title, author, genre, and publication date.
Author: This class should represent the author of a book. It should have attributes such as name, nationality, and date of birth.
Genre: This class should represent the genre of a book. It should have attributes such as name and description.
Library: This class should represent the library itself. It should have attributes such as name, address, and contact information. It should also have a collection of books.
The Library class should have the following methods:

add_book(book): This method should add a book to the library's collection.
remove_book(book): This method should remove a book from the library's collection.
get_book_by_title(title): This method should return a book from the library's collection by its title.
get_books_by_author(author): This method should return a list of books from the library's collection by their author.
get_books_by_genre(genre): This method should return a list of books from the library's collection by their genre.
The Library class should also have the following static methods:

get_all_books(): This method should return a list of all books in the library's collection.
get_number_of_books(): This method should return the number of books in the library's collection.
The Library class should also have a constructor and a destructor.

The Book, Author, and Genre classes should also have constructors and destructors.

The Book, Author, and Genre classes should also have methods to print their information.

The Library class should also have a method to print a list of all books in its collection.

The Library class should also have a method to search for a book by its title.

The Library class should also have a method to check out a book to a user.

The Library class should also have a method to check in a book from a user.

The Library class should also handle exceptions such as:

BookNotFoundError: This exception should be raised if a book is not found in the library's collection.
BookCheckoutError: This exception should be raised if a book is already checked out to another user.
BookCheckInError: This exception should be raised if a book is not checked out by any user.
The Library class should also have a decorator to decorate its checkout() and checkin() methods to ensure that only logged-in users can check out and check in books.

Additional topics that can be added to the problem:

Data hiding: The Book, Author, and Genre classes can be designed to encapsulate their data by using private instance variables and getter and setter methods.
Object cloning: The Book, Author, and Genre classes can be designed to support object cloning so that copies of objects can be created without modifying the original objects.
Collection of objects: The Library class can use a collection such as a list or a dictionary to store its collection of books.
Static attributes and methods: The Book, Author, Genre, and Library classes can use static attributes and methods to store and access information that is common to all objects of the class.
Super keyword: The Book, Author, and Genre classes can use the super keyword to call methods of their parent classes.
Method overwriting: The Book, Author, and Genre classes can overwrite methods of their parent classes to provide custom implementations.
Operator overloading: The Book, Author, and Genre classes can overload operators such as +, -, and == to implement custom behaviour for these operators.
Method overloading: The Book, Author, and Genre classes can overload methods to provide different implementations of the same method based on the number and types of parameters that are passed to the method.
Garbage collection: The Python garbage collector can be used to automatically manage the memory of objects.
Object printing: The Book, Author, and Genre classes can be designed to provide custom printing behaviour by implementing the str() and repr() methods.
Decorators: The Library class can use a decorator to decorate its checkout() and checkin() methods to ensure that only logged-in users can check out and check in books.


Now, here is the description of how this code works.

Library Management System in Python

This code implements a Python class hierarchy to model a library system. The system includes the following classes:

* Book: This class represents a book in the library. It has attributes such as title, author, genre, and publication date.
* Author: This class represents the author of a book. It has attributes such as name, nationality, and date of birth.
* Genre: This class represents the genre of a book. It has attributes such as name and description.
* Library: This class represents the library itself. It has attributes such as name, address, and contact information. It also has a collection of books.

The Library class has the following methods:

* add_book(book): This method adds a book to the library's collection.
* remove_book(book): This method removes a book from the library's collection.
* get_book_by_title(title): This method returns a book from the library's collection by its title.
* get_books_by_author(author): This method returns a list of books from the library's collection by their author.
* get_books_by_genre(genre): This method returns a list of books from the library's collection by their genre.

The Library class also has the following static methods::

* get_all_books(): This method returns a list of all books in the library's collection.
* get_number_of_books(): This method returns the number of books in the library's collection.

The Library class also has a constructor and a destructor.

The Book, Author, and Genre classes also have constructors and destructors.

The Book, Author, and Genre classes also have methods to print their information.

The Library class also has a method to print a list of all books in its collection.

The Library class also has a method to search for a book by its title.

The Library class also has a method to check out a book for a user.

The Library class also has a method to check in a book from a user.

The Library class also handles exceptions such as:

* BookNotFoundError: This exception is raised if a book is not found in the library's collection.
* BookCheckoutError: This exception is raised if a book is already checked out to another user.
* BookCheckInError: This exception is raised if a book is not checked out to any user.

The Library class also has a decorator to decorate its checkout() and checkin() methods to ensure that only logged-in users can check out and check in books.
