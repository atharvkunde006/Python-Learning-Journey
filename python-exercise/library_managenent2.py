print("Wellcome to our library")
class library:
    def __init__(self):
        self.books=[]
    
    def book(self,book):
        self.books.appent(book)
        
    def show(self):
        print(f"The books are {len(self.books)}This are the books")
        
s1=library()
n=int(input("number of books"))
for i in range(n):
  num=input(f"Enter the name of book{i+1}:")
s1.book(num)
s1.show
