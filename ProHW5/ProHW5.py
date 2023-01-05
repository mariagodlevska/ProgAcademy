# створити програму роботи з раціональними дробами зі всіма діями з ними

import math


class VulgarFractions:
    def __init__(self, a: int, b: int):
        if not b:
            raise ZeroDivisionError
        else:
            self.b = b

        self.a = a

    def minus_check(self):
        if self.a * self.b < 0:
            return abs(self.a) * -1
        else:
            return self.a

    def __add__(self, other):
        common_d = abs(self.b) * abs(other.b)
        numerator1 = self.minus_check() * (common_d // abs(self.b))
        numerator2 = other.minus_check() * (common_d // abs(other.b))
        numerator_f = numerator1 + numerator2

        return VulgarFractions(numerator_f, common_d)

    def __sub__(self, other):
        common_d = abs(self.b) * abs(other.b)
        numerator1 = self.minus_check() * (common_d // abs(self.b))
        numerator2 = other.minus_check() * (common_d // abs(other.b))
        numerator_f = numerator1 - numerator2

        return VulgarFractions(numerator_f, common_d)

    def __mul__(self, other):
        self_a = 1
        other_a = 1
        if self.a * self.b < 0:
            self_a *= -1
        if other.a * other.b < 0:
            other_a *= -1

        common_d = abs(self.b) * abs(other.b)
        numerator_f = self_a * abs(self.a) * other_a * abs(other.a)

        return VulgarFractions(numerator_f, common_d)

    def __truediv__(self, other):
        self_a = 1
        other_a = 1
        if self.a * self.b < 0:
            self_a *= -1
        if other.a * other.b < 0:
            other_a *= -1

        common_d = abs(self.b) * abs(other.a)
        numerator_f = (self_a * abs(self.a)) * (other_a * abs(other.b))

        return VulgarFractions(numerator_f, common_d)

    def __str__(self):
        a = abs(self.a // math.gcd(self.a, self.b))
        b = abs(self.b // math.gcd(self.a, self.b))

        if self.a * self.b < 0:
            minus = -1
        else:
            minus = 1

        if a > b and not a % b:
            return f'{minus * a//b}'
        elif a > b and a % b:
            return f'{minus * a // b}  {a - ((a // b) * b)}/{b}'

        if a == b:
            return f'{minus * 1}'

        if b == 1:
            return f'{minus * a}'

        return f'{minus * a}/{b}'


m1 = VulgarFractions(-2, 4)
m2 = VulgarFractions(3, 5)

print(m1-m2)
