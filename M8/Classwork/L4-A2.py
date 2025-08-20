class Library:
    def __init__(self,list_of_book ,name):
        self.bookslist = list_of_book
        self.name = name
        self.lenDict = {}

    def display_books(self):
        print(f"We have the following books in our library : {self}")
        for book in self.bookslist:
            print(book)
    def lend_book(self,user, book):
        if book in self.bookslist:
           print("Sorry, we do not have that book.")
        elif book in self.lenDict:
            print(f"The book is already being used by {self.lenDict[book]}.")
        else:
            self.lenDict[book] = user
            print("lender-book database has been updated. You can take the book now.")
    def add_book(self, book):
        self.bookslist.append(book)
        print(f"The book '{book}' has been added to the list.")
    def return_book(self, book):
        if book in self.lenDict:
            del self.lenDict[book]
            print(f"The book has been returned. Thank you!")
        else:
            print("This book was not borrowed from us.")
if __name__ == "__main__":
    books = Library(['Python',
                     'Java',
                     'C++',
                     'JavaScript'],
                     "Central Library")
    user_name = input("Welcome to our library! please enter your name: ")
    while True:
        print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")
        print("1. Display books\n2. Lend book\n3. Add book\n4. Return book\n5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            books.display_books()
        elif choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lend_book(user_name, book)
        elif choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.add_book(book)
        elif choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.return_book(book)
        elif choice == '5':
            print("Thank you for visiting the library!")
            break
        else:
            print("Invalid choice. Please try again.")