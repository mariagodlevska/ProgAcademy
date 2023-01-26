# 1) Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.

def dec_counter(func):

    def counter(*args, **kwargs):
        counter.count += 1
        return func(*args, **kwargs)

    counter.count = 0

    return counter


@dec_counter
def userfunc(n):
    return n*10


@dec_counter
def userfunc2(n):
    return n*11

print(userfunc(2))
print(userfunc(3))
print(userfunc2(2))
print(userfunc.count)

# 2) Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки последовательности.

listoffunc = []

def registrator(func):
    listoffunc.append(func)
    return func

@registrator
def userfunc3(n):
    return n*10

@registrator
def userfunc4(n):
    return n*30


print(userfunc3(2))
print(userfunc4(2))
print(listoffunc)


# 3) Предположим, в классе определен метод __str__, который возвращает строку на основании класса.
# Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл,
# имя которого совпадает с именем класса, метод которого вы декорировали.

def dec(func):
    def dec1(*args):
        name = f'{func.__qualname__}.txt'
        smth = func(*args)
        with open(name, 'a') as file:
            file.write(f'{smth}\n')
        return smth
    return dec1

@dec
class Hello:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Hello, {self.name}'

print(Hello('Bob'))

# 4) Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
# Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и
# в какой файл сохранить результаты хронометража. Цель - провести хронометраж декорируемой функции.

import time


def timecount(number=1, filename='timecount.txt'):
    def timecountdec(func):
        def timecountinn(*args, **kwargs):
            start = time.time()
            end = time.time()
            for i in range(number):
                result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                file.write(f'Start:{start}\nStop:{end}\nTime running:{end-start}\n\n')
            return result
        return timecountinn

    return timecountdec


class Prime:

    def __init__(self, n):
        self.n = n

    @timecount(100000000)
    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True


print(Prime(5).prime_numbers())
