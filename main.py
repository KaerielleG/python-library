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
    
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def display_info(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"

    def add_new_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter the author's name: ")
        author = self.find_author_by_name(name)
        if author:
            print(author.display_info())
        else:
            print(f"No author found with the name '{name}'.")

    def display_all_authors(self):
        if self.authors:
            for author in self.authors:
                print(author.display_info())
        else:
            print("No authors registered in the library.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def find_user_by_id(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None

    def find_author_by_name(self, name):
        for author in self.authors:
            if author.get_name().lower() == name.lower():
                return author
        return None
    def add_new_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter the author's name: ")
        author = self.find_author_by_name(name)
        if author:
            print(author.display_info())
        else:
            print(f"No author found with the name '{name}'.")

    def display_all_authors(self):
        if self.authors:
            for author in self.authors:
                print(author.display_info())
        else:
            print("No authors registered in the library.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def find_user_by_id(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None

    def find_author_by_name(self, name):
        for author in self.authors:
            if author.get_name().lower() == name.lower():
                return author
        return None
    
from menu import LibraryMenu

from lib.menu import LibraryMenu


if __name__ == "__main__":
    menu = LibraryMenu()
    menu.main_menu()
