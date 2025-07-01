class library :
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        print(f"Book added :{book}")
    def display_books(self):
        if self.no_of_books == 0:
            print("No books in the library")
        elif self.no_of_books > 0:
            print("Books in the library are : ")
            for book in self.books:
                print(f"-{book}")

    def count_books(self):
        print(f"Total number of books : {self.no_of_books}")
lib=library()
lib.add_book("Python")
lib.add_book("SQL")
lib.add_book("Fabric")
lib.display_books()
lib.count_books()

    
 