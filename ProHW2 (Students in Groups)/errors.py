#  raises an error if the group student limit is reached

class StudentNumberError(Exception):
    def __init__(self, student_number):
        self.student_number = student_number

    def __str__(self):
        return f'The limit of {self.student_number} is reached.'