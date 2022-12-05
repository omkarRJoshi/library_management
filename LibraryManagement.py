class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDic = {}

    def displayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDic.keys():
            self.lendDic.update({book:user})
            print("Lender-Book database has been updated, you can take your book now")
        else:
            print(F"book is already being used by {self.lendDic[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("book has beed added to the book list")

    def returnBook(self, book):
        # self.lendBook.remove(book)
        self.lendDic.pop(book)

if __name__ == '__main__':
    lib1 = Library(['book1', 'book2', 'book3', 'book4', 'book5'], 'libreary1')

    while(True):
        print(f"welcome to the {lib1.name} library. Enter your choice to cintinue")
        print("1. Display books")
        print("2. Lend a books")
        print("3. Add a books")
        print("4. Return a books")

        user_choice = int(input())

        if user_choice == 1:
            lib1.displayBook()
        elif user_choice == 2:
            book_name = input("Enter the name of the book you want to lend: ")
            user_name = input("Enter your name: ")
            lib1.lendBook(user_name, book_name)
        elif user_choice == 3:
            book_name = input("Enter a book name that you want add: ")
            lib1.addBook(book_name)
        elif user_choice == 4:
            book_name = input("enter a book name that you want to return: ")
            lib1.returnBook(book_name)
        else:
            print("not a valid option")

        print("Press q to quit and c to continue")
        termination = input()
        if termination == 'q':
            exit()

