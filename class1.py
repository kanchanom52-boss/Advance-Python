class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name

class Library:
    def issue(self, book, patron):
        if book.available:
            book.available = False
            print(book.name, "issued to", patron.name)
            
    def return_book(self, book):
        book.available = True
        print(book.name, "returned")


b1 = Book("Python")
p1 = Patron("Rahul")
lib = Library()
lib.issue(b1, p1)
lib.return_book(b1)
