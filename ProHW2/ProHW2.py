# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).

class Human:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'


# 2. На його основі створіть клас Студент (перевизначте метод виведення інформації).


class Student(Human):
    def __init__(self, name: str, surname: str):
        super(Student, self).__init__(name)
        self.surname = surname

    def __str__(self):
        return f'{super().__str__()} {self.surname}'


# 3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.


class Group:
    def __init__(self, group_name: str, student_number=10):
        self.group_name = group_name
        self.student_number = student_number
        self.__students = []

    def add_student(self, student):
        if student not in self.__students and len(self.__students) < self.student_number:
            self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

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

print(Math)

