# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії
# та кількість членів, що видаються послідовностю.
# Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.

def userfunc(n):
    return n*10


def genfunc(start: int, stop: int, userfunc):
    while start <= stop:
        yield userfunc(start)
        start += 1


for i in genfunc(1, 10, userfunc):
    print(i)


# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація
# https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.

def r_fib(n):
    if n <= 1:
        return n
    else:
        return r_fib(n-1) + r_fib(n-2)


for i in range(1, 10):
    print(r_fib(i))


print('***************')

def not_rec_fib(n):
    num = [0, 1]

    def cache(n):
        if n <= len(num):
            return n

        for i in range(n):
            num[-2] = num[-1]
            num[-1] = num[-2] + num[-1]
            num.append(num[-1])

        return num[-1]

    return cache(n)


for i in range(1, 10):
    print(not_rec_fib(i))

# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
# і поверне суми елементів отриманого списку.


def userfunc2(n):
    return n*11


def listeditor(li: list):
    s = 0
    for i in range(len(li)):
        s += userfunc2(i)
    return s


print(int(listeditor([1, 2, 3, 4, 5])))
