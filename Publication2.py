from Publication1 import Publication


class Date:
    def __init__(self, day: int, month: int, year: int):
        if isinstance(day, int) and 1 <= day <= 31:
            self.day = day
        else:
            raise ValueError('Invalid Date')
        if isinstance(month, int) and 1 <= month <= 12:
            self.month = month
        else:
            raise ValueError('Invalid Date')
        if isinstance(year, int) and 0 <= year <= 2023:
            self.year = year
        else:
            raise ValueError("Invalid date")

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


class Publication2(Publication):
    def __init__(self, title: str, price: float, date: Date) -> None:
        if isinstance(title, str) and isinstance(price, (int, float)):
            super().__init__(title, price)
        else:
            raise ValueError('Title must be string.Price must be float.')
        if isinstance(date, Date):
            self.date = date
        else:
            raise ValueError("The date must be Date type.")


class Book(Publication2):
    def __init__(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.page_count = input("Input the page count: ")
        day = int(input('Input the Day: '))
        month = int(input('Input the Month: '))
        year = int(input('Input the Year: '))
        date = Date(day, month, year)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.page_count = int(self.page_count)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def get_book(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.page_count = input("Input the page count: ")
        day = int(input('Input the Day: '))
        month = int(input('Input the Month: '))
        year = int(input('Input the Year: '))
        date = Date(day, month, year)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.page_count = int(self.page_count)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def put_book(self) -> None:
        print(f'Title: {self.title}. Price: {self.price}. Date: {self.date}. Page count: {self.page_count}')


class Tape(Publication2):
    def __init__(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.time = input("Input the page count: ")
        day = int(input('Input the Day: '))
        month = int(input('Input the Month: '))
        year = int(input('Input the Year: '))
        date = Date(day, month, year)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.time = int(self.time)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def get_tape(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.time = input("Input the page count: ")
        day = int(input('Input the Day: '))
        month = int(input('Input the Month: '))
        year = int(input('Input the Year: '))
        date = Date(day, month, year)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.time = int(self.time)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def put_tape(self) -> tuple:
        print(f'Title: {self.title}. Price: {self.price}. Date: {self.date}. Time: {self.time}')

try:
    book1 = Book()
    tape1 = Tape()
    book1.get_book()
    tape1.get_tape()
    book1.put_book()
    tape1.put_tape()
except ValueError as ve:
    print(str(ve))