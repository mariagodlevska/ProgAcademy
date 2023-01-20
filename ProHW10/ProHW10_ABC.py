# 1) Создайте ABC класс с абстрактным методом проверки целого числа на простоту.
# Т.е., если параметром этого метода является целое число и оно простое,
# то метод должен вернуть True, а в противном случае False.

# from abc import ABC, abstractmethod

import abc


class Prime(abc.ABC):

    @abc.abstractmethod
    def prime_numbers(self, n: int):
        if n is not int:
            return False
        for i in range(2, n):
            if n % i:
                return False

        return True


# 2) Создайте класс его наследующий.

class Smth1(Prime):

    def __init__(self, n):
        self.n = n

    def prime_numbers(self, n: int):
        if self.n is not int:
            return False
        for i in range(2, self.n):
            if self.n % i:
                return False

        return True


# 3) Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
# Зарегистрируйте его в качестве виртуального подкласса.


class Smth2:

    def __init__(self, n):
        self.n = n

    def prime_numbers(self):
        if self.n is not int:
            return False
        for i in range(2, self.n):
            if self.n % i:
                return False

        return True


Prime.register(Smth2)

m = Smth2(7)

# 4) Проверьте работоспособность проекта.　

print(isinstance(m, Prime))
print(Smth1(9))
print(Smth2.prime_numbers(11))

