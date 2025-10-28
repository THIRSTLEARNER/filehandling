class EmptyLibraryError(Exception):
    pass



class library:
    def __init__(self):
        self.books = {}
        self.borrow = []
    def add__books(self,title,author):
        self.books[title] = author
        print(title, "by ", author, "added to the library")
        print()
    def show(self):
            print("\n Current Library Collection:")
            for title, author in self.books.items():
                status = "Borrowed" if title in self.borrow else "Available"
                print(f' - "{title}" by {author} {status}')
            print()
    def borrow_books(self,title):
        if not self.books:
            raise EmptyLibraryError("Cannot borrow from an empty library.")
        if title not in self.books:
            raise KeyError(f'"{title}" does not exist in the library.')
        if title in self.borrow:
            print(f'"{title}" is already borrowed.')
        else:
            self.borrow.append(title)
            print(f'You borrowed "{title}".')
    def returnbooks(self,title):
        if title not in self.borrow:
            raise ValueError("BOOKS NOT BORROWED")
        self.borrow.remove(title)
        print(f'You returned "{title}".')


try:      
    obj = library()
    obj.add__books("mocking","ranner")
    obj.add__books("seven deadly sins","austin")
    obj.add__books("blackclover","dencyrus")

    obj.borrow_books("blackclover")
    obj.returnbooks("blackclover")
    obj.borrow_books("seven deadly sins")
    obj.borrow_books("ang aking tula")
    obj.show()

except(KeyError, ValueError, EmptyLibraryError) as e:
    print("ERROR TRY AGAIN",e)