import logging
import errors

# class Group with such functions: add student, remove student, search student

class Group:
    def __init__(self, group_name: str, student_number=10):
        self.group_name = group_name
        self.student_number = student_number
        self.__students = []

    def add_student(self, student):
        if not len(self.__students) < self.student_number:
            logging.error(errors.StudentNumberError(self.student_number))
            raise errors.StudentNumberError(self.student_number)
        elif student not in self.__students and len(self.__students) < self.student_number:
            self.__students.append(student)
            logging.info(f'Student {student} was added to the group.')

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            logging.info(f'Student {student} was removed from the group.')

    def search_student(self):
        for student in self.__students:
            if student.surname == student:
                return student

    def __str__(self):
        return f'{self.group_name}\n' + '-'*20 + '\n' + '\n'.join(map(str, self.__students)) + '\n' + '-'*20 + '\n'
