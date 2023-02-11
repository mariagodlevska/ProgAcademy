# 1) Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.

class Registrator:
    registered_classes = []

    def __init__(self, regclass):
        self.regclass = regclass

    def __call__(self, *args, **kwargs):
        if self.regclass not in self.registered_classes:
            self.registered_classes.append(self.regclass)
        return self.regclass(*args, **kwargs)


@Registrator
class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Hello, {self.name}'


print(Name('Bob'))
print(Name.registered_classes)

# 2) Создайте декоратор класса с параметром.
# Параметром должна быть строка, которая должна дописываться (слева) к результату работы метода __str__.


class AddStrLeft:

    def __init__(self, string):
        self.string = string

    def __call__(self, func):
        def inner(*args, **kwargs):
            return self.string + func(*args, **kwargs)
        return inner


class Name1:
    def __init__(self, name):
        self.name = name

    @AddStrLeft('Greetings, ')
    def __str__(self):
        return f'{self.name}'


print(Name1('Bob'))


# 3) Для класса Box напишите статический метод,
# который будет подсчитывать суммарный объем двух ящиков, которые будут его параметрами.

class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def volume_sum(box1, box2):
        return box1.volume() + box2.volume()


box1 = Box(2, 3, 4)
box2 = Box(5, 6, 7)

print(Box.volume_sum(box1, box2))
