# class Human describes the name of the student, and class Student describes the surname

class Human:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Student(Human):
    def __init__(self, name: str, surname: str):
        super(Student, self).__init__(name)
        self.surname = surname

    def __str__(self):
        return f'{super().__str__()} {self.surname}'
