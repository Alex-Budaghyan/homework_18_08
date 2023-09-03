from collections.abc import Sequence


class Course:
    def __init__(self, name: str, credit: int) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string.')
        if isinstance(credit, int):
            self.credit = credit
        else:
            raise ValueError('Credit must be integer.')
        self.students = []

    def add_student(self, student: str) -> None:
        self.students.append(student)

    def __str__(self) -> str:
        return f'Course: {self.name}. Credits: {self.credit}. Students: {self.students}'


class Departament:
    def __init__(self, name: str, courses: (Course, Sequence)) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string.')
        if isinstance(courses, Course):
            self.courses = courses
        elif isinstance(courses, Sequence) and all(isinstance(i, Course) for i in courses):
            self.courses = list(courses)
        else:
            raise ValueError('Course must be Sequence or Course type.')

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def remove_course(self, course: Course) -> None:
        self.courses.remove(course)

    def __str__(self) -> str:
        return f'Department: {self.name}.   Courses: {[course.__str__() for course in self.courses]}'


course1 = Course('Design', 2)
course2 = Course('C#', 3)
course3 = Course('Python', 9)
student1 = 'James'
student2 = 'Arman'
try:
    course1.add_student(student1)
    course3.add_student(student2)
    print(course2)
    print(course3)
    d = Departament('YSU', (course3, course2))
    d.add_course(course1)
    d.remove_course(course2)
    print(d)
except ValueError as ve:
    print(ve)
