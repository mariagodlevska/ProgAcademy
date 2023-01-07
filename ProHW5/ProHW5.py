# створити програму роботи з раціональними дробами зі всіма діями з ними

class VulgarFractions:
    def __init__(self, a: int, b: int):
        if not b:
            raise ZeroDivisionError
        else:
            self.b = b

        self.a = a

    def minus_check(self):
        """

        :return: correct fraction sign
        """
        if self.a * self.b < 0 or self.a < 0 or self.b < 0:
            return abs(self.a) * -1
        else:
            return self.a

    def __add__(self, other):
        """

        :param other:
        :return: sum of two fractions
        """
        if abs(self.a//self.b) == abs(other.a//other.b):
            return f'{(self.a * other.a)//(self.b * other.b)}'

        common_d = abs(self.b) * abs(other.b)
        numerator1 = self.minus_check() * (common_d // abs(self.b))
        numerator2 = other.minus_check() * (common_d // abs(other.b))
        numerator_f = numerator1 + numerator2

        return VulgarFractions(numerator_f, common_d)

    def __sub__(self, other):
        """

        :param other:
        :return: substitution of two fractions
        """
        if abs(self.a//self.b) == abs(other.a//other.b):
            return f'{(self.a * other.a)//(self.b * other.b)}'

        common_d = abs(self.b) * abs(other.b)
        numerator1 = self.minus_check() * (common_d // abs(self.b))
        numerator2 = other.minus_check() * (common_d // abs(other.b))
        numerator_f = numerator1 - numerator2

        return VulgarFractions(numerator_f, common_d)

    def __mul__(self, other):
        """

        :param other:
        :return: multiplication of two fractions
        """
        if abs(self.a//self.b) == abs(other.a//other.b):
            return f'{(self.a * other.a)//(self.b * other.b)}'

        common_d = abs(self.b) * abs(other.b)
        # numerator_f = self.minus_check() * abs(self.a) * other.minus_check() * abs(other.a)
        numerator_f = self.minus_check() * other.minus_check()

        return VulgarFractions(numerator_f, common_d)

    def __truediv__(self, other):
        """

        :param other:
        :return: true division of two fractions
        """
        if abs(self.a//self.b) == abs(other.a//other.b):
            return f'{(self.a * other.a)//(self.b * other.b)}'

        common_d = abs(self.b) * other.a
        numerator_f = self.a * abs(other.b)

        return VulgarFractions(numerator_f, common_d)

    def __str__(self):
        a = self.a
        b = self.b

        if (a * b) < 0:
            minus = '-'
        else:
            minus = ''

        if abs(a) > abs(b) and not (a % b):
            return f'{minus}{abs(a) // abs(b)}'

        elif abs(a) > abs(b) and (a % b):
            return f'{minus}{abs(a) // abs(b)} {(abs(a) - ((abs(a) // abs(b)) * abs(b)))}/{abs(b)}'

        elif abs(a) < abs(b):
            return f'{minus}{abs(a)}/{abs(b)}'

        if b == 1:
            return f'{minus}{abs(a)}'

        if a == b:
            return f'{minus}1'


m1 = VulgarFractions(-5, 2)
m2 = VulgarFractions(3, 6)

print(f'{m1.a}/{m1.b} + {m2.a}/{m2.b}')
print(m1-m2)

