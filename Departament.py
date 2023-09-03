from collections.abc import Sequence


class Department:
    def __init__(self, name: str) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string.')
        self.employees = []

    def add_employees(self, employees: (Sequence, str)) -> None:
        if isinstance(employees, str):
            self.employees.append(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees.extend(employees)
        else:
            raise ValueError('Employees must be string or Sequence or string.')

    def list_department_details(self) -> str:
        return f'Department: {self.name}. Employees: {self.employees}\n'


class Company:
    def __init__(self, name: str, departments: (str, Sequence), employees: (Sequence, str)) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string')
        if isinstance(departments, str):
            self.departments = departments
        elif isinstance(departments, Sequence) and all(isinstance(i, Department) for i in departments):
            self.departments = list(departments)
        else:
            raise ValueError("Projects must be string type or sequence of strings")

        if isinstance(employees, str):
            self.employees = employees
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees = list(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def add_project(self, department: Department) -> None:
        self.departments.append(department)

    def remove_project(self, department: Department) -> None:
        self.departments.remove(department)

    def add_employees(self, department: Department, employees: (Sequence, str)) -> None:
        if isinstance(employees, str):
            self.departments[self.departments.index(department)].add_employees(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.departments[self.departments.index(department)].add_employees(list(employees))
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def __str__(self) -> str:
        s1 = f'Company: {self.name}.\n'
        for department in self.departments:
            s1 += department.list_department_details()
        return s1


try:
    d1 = Department('C++')
    d2 = Department('Python')
    company1 = Company('Piscart', (d1, d2), ('Aram', 'Hayk'))
    company1.add_employees(d1, 'James')
    company1.add_employees(d2, ('Davit', 'Vardan', 'Gevorg'))
    print(company1)
except ValueError as ve:
    print(str(ve))

