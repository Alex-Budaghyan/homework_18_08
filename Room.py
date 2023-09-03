class Room:
    def __init__(self, name: str, occupied: bool, capacity: int) -> None:
        if isinstance(name, str) and isinstance(capacity, int):
            self.number = name
            self.capacity = capacity
        if isinstance(occupied, bool):
            self.occupied = occupied

    def occupied_room(self) -> None:
        if not self.occupied:
            self.occupied = True
        else:
            raise ValueError('The room is occupied.')


class Course:
    def __init__(self, name: str, num_students: int) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string.')
        if isinstance(num_students, int):
            self.num_students = num_students
        else:
            raise ValueError("Number of students must be integer.")


try:
    r1 = Room('Ada Lovelace', False, 60)
    r2 = Room('Donald Knuth', False, 20)
    course1 = Course('Pyhton', 26)
    course2 = Course('Java', 30)
    if not r1.occupied and course1.num_students <= r1.capacity:
        r1.occupied_room()
    if not r2.occupied and course2.num_students <= r2.capacity:
        r2.occupied_room()
    print(r1.occupied)
    print(r2.occupied)
except ValueError as ve:
    print(str(ve))

