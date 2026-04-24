print("Welcome to the Library")


class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def show(self):
        print(f"The library has {self.nobooks} books. The books are:")
        for book in self.books:
            print(book)


l1 = Library()
l1.addbook("Atharv 1")
l1.addbook("Atharv 2")
l1.addbook("Atharv 3")
l1.show()