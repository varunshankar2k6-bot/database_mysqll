class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Book: {self.title}, Author: {self.author}")
# Inheritance function
class Online_Book(Book):
    def display(self):
        print(f"Online-Book: {self.title}, Author: {self.author}")
class HardCopy(Book):
    def display(self):
        print(f"Hard Copy Book: {self.title}, Author: {self.author}")
# Encapsulation function
class Library:
    def __init__(self):
        self.__books = []      
    def add_book(self, book):
        self.__books.append(book)
    def show_books(self):
        for book in self.__books:
            book.display()     
# Objects
b1 = Online_Book("Python", "V")
b2 = HardCopy("JAVA", "S")
library = Library()
library.add_book(b1)
library.add_book(b2)
library.show_books()