class Person:
    def __init__(self, name: str, age: int) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string.')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age must be intenger.')

    def set_name(self, n: str) -> None:
        if isinstance(n, str):
            self.name = n
        else:
            raise ValueError('Name must be string.')

    def set_age(self, age: int) -> None:
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age must be integer.')

    def print_Person(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}')


class Employee(Person):
    def __init__(self, name: str, age: int, id: int, department: str) -> None:
        if isinstance(name, str) and isinstance(age, int):
            super().__init__(name, age)
        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError('Person ID must be integer.')
        if isinstance(department, str):
            self.department = department
        else:
            raise ValueError('Department must be string.')

    def set_id(self, id: int) -> None:
        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError('Person ID must be integer.')

    def set_department(self, department):
        if isinstance(department, str):
            self.department = department
        else:
            raise ValueError('Department must be string.')

    def print_Employee(self) -> None:
        print(f'Name: {self.name}. Age: {self.age}. ID: {self.id}. Department: {self.department}')


try:
    employee1 = Employee('James', 25, 41, 'Python')
    p = Person('James', 47)
    employee2 = Employee('Aram', 21, 100, 'Java')
    p.set_age(48)
    employee1.set_id(101)
    employee2.set_department('C++')
    employee1.set_age(30)
    p.print_Person()
    employee1.print_Employee()
    employee2.print_Employee()
except ValueError as ve:
    print(str(ve))
