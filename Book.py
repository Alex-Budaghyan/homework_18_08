from collections.abc import Sequence


class Book:
    def __init__(self, title: str, author: str) -> None:
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError('Title must be a string.')
        if isinstance(author, str):
            self.author = author
        else:
            raise ValueError('Author must be a string.')
        self.libraries = []

    def add_to_library(self, library) -> None:
        library.add_book(self)
        self.libraries.append(library)

    def list_libraries(self):
        for i in self.libraries:
            print(i.name)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self, name: str, book_ls: (Book, Sequence)) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be a string.')
        if isinstance(book_ls, Book):
            self.book_ls = [book_ls]
        elif isinstance(book_ls, Sequence) and all(isinstance(i, Book) for i in book_ls):
            self.book_ls = list(book_ls)
        else:
            raise ValueError('Book list must be a Sequence of Book type.')

    def add_book(self, book) -> None:
        self.book_ls.append(book)

    def remove_book(self, book) -> None:
        self.book_ls.remove(book)

    def __str__(self) -> str:
        return f'Library: {self.name}.\nBooks: {[i.__str__() for i in self.book_ls]}'


book1 = Book('Little', 'Edward Carey')
book2 = Book('Hamlet', 'Maggie O’Farrell')
book3 = Book('Wolf Hall', 'Hilary Mantel')
book4 = Book('Brief Answers to the Big Questions', 'Stephen Hawking')
book5 = Book("Homo Deus", " Yuval Noah Harari")
book6 = Book('THE ACCIDENTAL UNIVERSE', 'Alan Lightman')
try:
    lb1 = Library('Historical', (book1, book3))
    lb2 = Library('Science', (book4, book6))
    print(lb1)
    lb1.add_book(book2)
    lb1.remove_book(book1)
    print(lb1)
    book5.add_to_library(lb2)
    lb2.remove_book(book5)
    print(lb2)
except ValueError as v:
    print(v)
    