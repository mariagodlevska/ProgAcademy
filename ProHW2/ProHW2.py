# 2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів,
# викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).
# Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(filename='LogFile.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

logging.info('Started')


class StudentNumberError(Exception):
    def __init__(self, student_number):
        self.student_number = student_number

    def __str__(self):
        return f'The limit of {self.student_number} is reached.'

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


class Group:
    def __init__(self, group_name: str, student_number=10):
        self.group_name = group_name
        self.student_number = student_number
        self.__students = []

    def add_student(self, student):
        if not len(self.__students) < self.student_number:
            logging.error(StudentNumberError(self.student_number))
            raise StudentNumberError(self.student_number)
        elif student not in self.__students and len(self.__students) < self.student_number:
            self.__students.append(student)
            logging.info(f'Student {student} was added to the group.')

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            logging.info(f'Student {student} was removed from the group.')

    def search_student(self, student):
        for student in self.__students:
            if student.surname == student:
                return student

    def __str__(self):
        return f'{self.group_name}\n' + '-'*20 + '\n' + '\n'.join(map(str, self.__students)) + '\n' + '-'*20 + '\n'


Math = Group('Math', student_number=10)

Math.add_student(Student('Petro', 'Poroshenko'))
Math.add_student(Student('Volodymyr', 'Zelenskiy'))
Math.add_student(Student('Victor', 'Yushchenko'))
Math.add_student(Student('Petro1', 'Poroshenko'))
Math.add_student(Student('Volodymyr', '2Zelenskiy'))
Math.add_student(Student('Victor', '2Yushchenko'))
Math.add_student(Student('Petro3', 'Poroshenko'))
Math.add_student(Student('Volodymyr4', 'Zelenskiy'))
Math.add_student(Student('Victor7', 'Yushchenko'))
Math.add_student(Student('Petro4', 'Poroshenko'))
Math.add_student(Student('Volodymyr8', 'Zelenskiy'))
Math.add_student(Student('Victor9', 'Yushchenko'))

print(Math)

logging.info('Finished')
