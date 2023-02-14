# 1) Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.

class ReadOnlyDescriptor:

    def __init__(self, x):
        self.x = x

    def __get__(self, *args, **kwargs):
        return self.x

    def __set__(self, *args, **kwargs):
        raise ValueError('Read only parameter')

    def __delete__(self, *args, **kwargs):
        raise ValueError('Read only parameter')


class AB:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    nice = ReadOnlyDescriptor('Nice!')


ab = AB(4, 5)
print(ab.nice)

# 2) Реализуйте функционал, который будет запрещать установку полей класса любыми значениями,
# кроме целых чисел. Т.е., если тому или иному полю попытаться присвоить, например, строку,
# то должно быть возбужденно исключение.


class Integer:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Only integer allowed.")
        self.__dict__[key] = value


ab1 = Integer(5, 6)
# ab1.nice = 'Nice!'
ab1.number = 6

# 3) Реализуйте свойство класса, которое обладает следующим функционалом:
# при установки значения этого свойства в файл с заранее определенным названием
# должно сохранятся время (когда устанавливали значение свойства) и установленное значение.

import datetime


class DateTimeValue:

    def __init__(self, a):
        self.a = a

    def __get__(self, b, classvalue):
        return self.a

    def __set__(self, b, value):
        with open('date_time_value.txt', 'a') as f:
            f.write(f'Value = {self.a}, Time: {datetime.datetime.now()}\n')
            self.a = value

    def __delete__(self, b):
        del self.a


class AB1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    nice = DateTimeValue('Nice!')


ab2 = AB1(3, 5)
print(ab2.nice)
ab2.nice = 'Cool'
ab2.nice = 'Perfect'
