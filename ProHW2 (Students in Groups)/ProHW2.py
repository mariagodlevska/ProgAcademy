# Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
# Переконайтеся у працездатності проєктів.

import logging
import group
import student


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(filename='LogFile.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

logging.info('Started')

# test group with students

Math = group.Group('Math', student_number=10)

Math.add_student(student.Student('Petro', 'Poroshenko'))
Math.add_student(student.Student('Volodymyr', 'Zelenskiy'))
Math.add_student(student.Student('Victor', 'Yushchenko'))
Math.add_student(student.Student('Petro1', 'Poroshenko'))
Math.add_student(student.Student('Volodymyr', '2Zelenskiy'))
Math.add_student(student.Student('Victor', '2Yushchenko'))
Math.add_student(student.Student('Petro3', 'Poroshenko'))
Math.add_student(student.Student('Volodymyr4', 'Zelenskiy'))
# Math.add_student(student.Student('Victor7', 'Yushchenko'))
# Math.add_student(student.Student('Petro4', 'Poroshenko'))
# Math.add_student(student.Student('Volodymyr8', 'Zelenskiy'))
# Math.add_student(student.Student('Victor9', 'Yushchenko'))

# print(Math)

for i in Math:
    print(i)

logging.info('Finished')
