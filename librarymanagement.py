class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = False

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_borrowed(self):
        return self.__is_borrowed

    # Setters
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def display_info(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        return (f"Title: {self.__title}, Author: {self.__author}, "
                f"Genre: {self.__genre}, Published: {self.__publication_date}, Status: {status}")
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Methods
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        return False

    def display_info(self):
        books = ", ".join(self.__borrowed_books) if self.__borrowed_books else "None"
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {books}"
