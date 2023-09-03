class Publication:
    def __init__(self, title: str, price: float) -> None:
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError('Title must be string.')
        if isinstance(price, (float, int)):
            self.price = float(price)
        else:
            raise ValueError('Price must be float.')

    def get_data(self, title: str, price: (float, int)):
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError('Title must be string.')
        if isinstance(price, (float, int)):
            self.price = float(price)
        else:
            raise ValueError('Price must be float.')

    def put_data(self):
        print(f'Title: {self.title}. Price: {self.price}')


class Book(Publication):
    def __init__(self, title: str, price: float, page_count: int) -> None:
        if isinstance(title, str) and isinstance(price, (int, float)):
            super().__init__(title, price)
        else:
            raise ValueError('Title must be string.Price must be float.')
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise ValueError('Page count must be integer.')

    def get_book(self, title: str, price: float, page_count: int) -> None:
        if isinstance(title, str) and isinstance(price, (int, float)):
            super().get_data(title, price)
        else:
            raise ValueError('Title must be string.Price must be float.')
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise ValueError('Page count must be integer.')

    def put_book(self):
        print(f'Title: {self.title}. Price: {self.price}. Page count: {self.page_count}')


class Tape(Publication):
    def __init__(self, title: str, price: float, time: float) -> None:
        if isinstance(title, str) and isinstance(price, (int, float)):
            super().__init__(title, price)
        else:
            raise ValueError('Title must be string.Price must be float.')
        if isinstance(time, (float, int)):
            self.time = float(time)
        else:
            raise ValueError('Page count must be integer.')

    def get_tape(self, title: str, price: float, time: float):
        if isinstance(title, str) and isinstance(price, (int, float)):
            super().get_data(title, price)
        else:
            raise ValueError('Title must be string.Price must be float.')
        if isinstance(time, (float, int)):
            self.time = float(time)
        else:
            raise ValueError('Page count must be integer.')

    def put_tape(self):
        print(f'Title: {self.title}. Price: {self.price}. Time: {self.time}')


def main():
    try:
        book1 = Book('Book1', 10.25, 50)
        tape1 = Tape('C++ book', 20, 100)
        book1.get_book('Book C#', 20.85, 200)
        tape1.get_tape('Python book', 15.5, 880)
        book1.put_book()
        tape1.put_tape()
    except ValueError as ve:
        print(str(ve))


if __name__ == "__main__":
    main()