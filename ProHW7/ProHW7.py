# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
# Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу,
# або при передачі команди на завершення.


def geometric_prog(d: int, end_fun, element=1):
    for i in range(end_fun):
        yield element
        element *= d


for i in geometric_prog(3, 100):
    if i > 200000:
        geometric_prog(3, 10).close()
    else:
        print(i)

# 2. Реалізуйте свій аналог генераторної функції range().


def new_range(stop: int, start=1, step=1):
    while start <= stop:
        yield start
        start += step


for i in new_range(200, 2, 10):
    print(i)

# 3. Напишіть функцію-генератор, яка повертатиме прості числа.
# Верхня межа діапазону повинна бути задана параметром цієї функції.
import timeit


def prime_numbers(finish=100, start=2):
    num_list = [2]

    for start in range(start, finish):
        for i in num_list:
            if not start % i:
                break
        else:
            yield start
            num_list.append(start)


h = []
for n in prime_numbers(100):
    h.append(n)
print(h)


def prime_num1(finish=100, start=2):
    yield 1
    not_num_list = []
    # num_list = list(range(1, finish))
    while start < finish:
        if start in not_num_list:
            start += 1

        else:
            for i in range(start*start, finish+1, start):
                not_num_list.append(i)
            yield start
            start += 1


# b = []
# for n in prime_num1(100):
#     b.append(n)
# print(b)


def prime_num2(finish=100, start=2):
    yield 1
    not_num_list = []
    num_list = list(range(1, finish))
    while start < finish:
        if start not in num_list:
            start += 1

        else:
            for i in range(start * start, finish + 1, start):
                if i in num_list:
                    num_list.remove(i)
            yield start
            start += 1


d = []
for n in prime_num2(100):
    d.append(n)
print(d)


# 4. Напишіть генераторний вираз для заповнення списку.
# Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.

def cubus(finish):
    cubes = []
    for start in range(2, finish+1):
        yield start ** 3
        cubes.append(start ** 3)
    return cubes


for i in cubus(10):
    print(i)
