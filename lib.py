#Defining class Book,Member and Library
class Book:
    def __init__(self, title):
        self.title = title
class Member:
    def __init__(self, name):
        self.name = name
class Library:
    def __init__(self):
        self.books = []
        self.members = []
#Defining all the methods in the menu
    def add_book(self):
        title = input("Enter book title: ")
        book = Book(title)
        self.books.append(book)
        print("Book added")
    def register_member(self):
        name = input("Enter member name: ")
        member = Member(name)
        self.members.append(member)
        print("Member registered")
    def search_book(self):
        title = input("Enter book title to search: ")
        for book in self.books:
            if book.title == title:
                print("Book found")
            else:
                print("Book not found")
    def display_books(self):
        print("Books:")
        for book in self.books:
            print(book.title)
    def display_members(self):
        print("Members:")
        for member in self.members:
            print(member.name)

#Creating library object
library = Library()
#Infinite loop for menu till user exits
while True:
    print("1. Add Book")
    print("2. Register Member")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Display Members")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.register_member()
    elif choice == 3:
        library.search_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        library.display_members()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")