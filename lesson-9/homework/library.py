import csv
import os

class BookNotFoundException(Exception):
    """Exception raised when a book is not found"""
    def __init__(self, book, message = "Book not found!"):
        self.book = book 
        self.message = message
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    """Exception raised when the book is already borrewed"""
    def __init__(self, book, message = "Book is already borrowed!"):
        self.book = book
        self.message = message
        super().__init__(self.message) 

class MemberLimitExceededException(Exception):
    """Exception raised when the user tries to borrow more than he is allowed to do"""
    def __init__(self, message = "Members cannot borrow more that 3 books!"):
        super().__init__(message) 

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed 

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, title):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(title)
        else:
            raise MemberLimitExceededException()
        
    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)

class Library:
    def __init__(self, filename = "books.csv"):
        self.filename = filename
        self.books = self.load_books()
        self.members = {}

    def add_member(self, name):
        if name in self.members:
            print(f"Member '{name}' already exists!")
        else:
            self.members[name] = Member(name)
            print(f"Member '{name}' added successfully!")
            print("- "*15)

    def load_books(self):
        books = {}

        if not os.path.exists(self.filename):
            return books

        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books[row["title"]] = {
                    "author": row["author"],
                    "is_borrowed": row["is_borrowed"].lower() == "true"
                }
        return books
    
    def save_books(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ["title", "author", "is_borrowed"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in self.books.items():
                writer.writerow({
                    "title": title,
                    "author": details["author"],
                    "is_borrowed": details["is_borrowed"] 
                })

    def add_book(self, title, author):
        self.books[title] = {"author": author, "is_borrowed": False}
        self.save_books() 

    def borrow_books(self, member_name, title):
        if title in self.books and not self.books[title]["is_borrowed"]:
            if member_name not in self.members:
                self.members[member_name] = Member(member_name) 
            member = self.members[member_name]
            if len(member.borrowed_books) < 3:
                self.books[title]["is_borrowed"] = True
                member.borrow_book(title)
                self.save_books()
                print(f"{member_name} borrowed '{title}'.")
            else:
                raise MemberLimitExceededException()
        else:
            raise BookNotFoundException(title) 

    def return_books(self, member_name, title):
        if member_name not in self.members:
            print(f"Member {member_name} does not exist")
            return
        
        member = self.members[member_name]

        if title not in member.borrowed_books:
            print(f"'{title}' was not borrowed by this member")
            return
        
library = Library()

while True:
    print("1.Add a member")
    print("2.Add a book")
    print("3.Borrow a book")
    print("4.Return a book")
    print("5.Exit")
    print("* "*15)

    while True:
        try:
            option = int(input("Choose an option:"))
            break
        except ValueError:
            print("Enter a number only (1-5): \n")

    if option == 1:
        name = input("Enter member name: ")
        library.add_member(name)

    elif option == 2:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        library.add_book(title, author)

    elif option == 3:
        name = input("Enter member name: ")
        title = input("Enter the name of the book you want to borrow: ")
        library.borrow_books(name, title)

    elif option == 4:
        name = input("Enter member name: ")
        title = input("Enter the name of the book you want to return: ")

    elif option == 5:
        break

print("The program has finished working!")