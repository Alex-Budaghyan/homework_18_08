from collections.abc import Sequence


class Project:
    def __init__(self, name: str, description: str) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string')
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError('Description must be string.')
        self.employees = []

    def add_employee(self, employees: (Sequence, str)) -> None:
        if isinstance(employees, str):
            self.employees.append(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees.extend(employees)
        else:
            raise ValueError('Employees must be string or Sequence.')

    def list_project_details(self):
        return f'Project: {self.name}.\n"""{self.description}""".\nEmployees: {self.employees}'

    def __str__(self):
        return self.list_project_details()
class Company:
    def __init__(self, name: str, projects: (str, Sequence), employees: (Sequence, str)) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string')
        if isinstance(projects, str):
            self.projects = projects
        elif isinstance(projects, Sequence) and all(isinstance(i, Project) for i in projects):
            self.projects = list(projects)
        else:
            raise ValueError("Projects must be string type or sequence of strings")

        if isinstance(employees, str):
            self.employees = employees
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees = list(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def add_project(self, project: Project) -> None:
        self.projects.append(project)

    def remove_project(self, project: Project) -> None:
        self.projects.remove(project)

    def add_employees(self, project: Project, employees: (Sequence, str)) -> None:
        if isinstance(employees, str):
            self.projects[self.projects.index(project)].add_employee(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.projects[self.projects.index(project)].add_employee(list(employees))
        else:
            raise ValueError("Employees must be string  or Sequence of strings.")

    def __str__(self) -> None:
        s1 = f'Company: {self.name}.\n'
        for project in self.projects:
            s1 += project.list_project_details()
            s1 += '\n'
        return s1


try:
    p1 = Project('Project 1', 'Bank account')
    p2 = Project('Project 2', 'Library account')
    c1 = Company('Shift', (p1, p2), ('Hayk', 'Aram'))
    c1.add_employees(p1, ('Armen', 'James'))
    print(c1)
    print(p2)
except ValueError as ve:
    print(str(ve))