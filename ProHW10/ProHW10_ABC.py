# 1) Создайте ABC класс с абстрактным методом проверки целого числа на простоту.
# Т.е., если параметром этого метода является целое число и оно простое,
# то метод должен вернуть True, а в противном случае False.

import abc


class Prime(abc.ABC):

    @abc.abstractmethod
    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True


# 2) Создайте класс его наследующий.

class Smth1(Prime):

    def __init__(self, n):
        self.n = n

    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True


# 3) Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
# Зарегистрируйте его в качестве виртуального подкласса.


class Smth2:

    def __init__(self, n):
        self.n = n

    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True


Prime.register(Smth2)

m = Smth2(7)

# 4) Проверьте работоспособность проекта.　

print(isinstance(m, Prime))
print(Smth1(5).prime_numbers())
print(Smth2(10).prime_numbers())

