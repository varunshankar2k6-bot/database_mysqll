class Item:
    def display(self):
        pass
class Book(Item):
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self._author = author      # Protected variable
        self.year = year
        self.__copies = copies     # Private variable
    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self._author)
        print("Year:", self.year)
        print("Copies:", self.__copies)
    def get_copies(self):
        return self.__copies
class Member(Item):
    def __init__(self, member_id, name):
        self.__member_id = member_id    # Private variable
        self.name = name
    def display(self):
        print("Member ID:", self.__member_id)
        print("Name:", self.name)
    def get_member_id(self):
        return self.__member_id
class Library:
    # Static Variable
    library_name = "British Library"
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self):
        book_id = input("Enter Book ID: ")
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists")
                return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = int(input("Enter Year: "))
        copies = int(input("Enter Copies: "))
        book = Book(book_id, title, author, year, copies)
        self.books.append(book)
        print("Book Added")
    def register_member(self):
        member_id = input("Enter Member ID: ")
        for member in self.members:
            if member.get_member_id() == member_id:
                print("Member ID already exists")
                return
        name = input("Enter Member Name: ")
        member = Member(member_id, name)
        self.members.append(member)
        print("Member Registered")
    def search_book(self):
        book_id = input("Enter Book ID to Search: ")
        for book in self.books:
            if book.book_id == book_id:
                print("Book Found")
                book.display()
                return
        print("Book Not Found")
    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available")
        else:
            for book in self.books:
                book.display()
    def display_members(self):
        if len(self.members) == 0:
            print("No Members Registered")
        else:
            for member in self.members:
                member.display()
library = Library()
print("Library Name:", Library.library_name)
while True:
    print("1. Add Book")
    print("2. Register Member")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Display Members")
    print("6. Exit")
    choice = int(input("Enter Choice: "))
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