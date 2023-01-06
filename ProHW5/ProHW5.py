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
        """

        :return: correct fraction sign
        """
        if self.a * self.b < 0:
            return abs(self.a) * -1
        else:
            return self.a

    def __add__(self, other):
        """

        :param other:
        :return: sum of two fractions
        """
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
        common_d = abs(self.b) * abs(other.b)
        numerator_f = self.minus_check() * abs(self.a) * other.minus_check() * abs(other.a)

        return VulgarFractions(numerator_f, common_d)

    def __truediv__(self, other):
        """

        :param other:
        :return: true division of two fractions
        """
        common_d = abs(self.b) * abs(other.a)
        numerator_f = (self.minus_check() * abs(self.a)) * (other.minus_check() * abs(other.b))

        return VulgarFractions(numerator_f, common_d)

    def whole_number(self):
        """

        :return: whole number extracted from the fraction;
                 fraction numerator;
                 fraction denominator
        """
        a = self.a
        b = self.b

        if (a * b) < 0:
            minus = -1
        else:
            minus = 1

        if abs(a) > abs(b) and not (a % b):
            return (minus * abs(a) // abs(b)), '', ''

        elif abs(a) > abs(b) and (a % b):
            return (minus * abs(a) // abs(b)), (abs(a) - ((abs(a) // abs(b)) * abs(b))), abs(b)

        elif abs(a) < abs(b):
            return '', (minus * abs(a)), abs(b)

        if a == b:
            return (minus * 1), 1, 1

        if b == 1:
            return (minus * abs(a)), 1, 1

    def __str__(self):
        # a = abs(self.whole_number()[2] // math.gcd(self.whole_number()[1], self.whole_number()[2]))
        # b = abs(self.whole_number()[2] // math.gcd(self.whole_number()[1], self.whole_number()[2]))
        a=9
        b=5
        # if self.a * self.b < 0:
        #     minus = -1
        # else:
        #     minus = 1
        #
        # if a > b and not a % b:
        #     return f'{minus * a//b}'
        # elif a > b and a % b:
        #     return f'{minus * a // b}  {a - ((a // b) * b)}/{b}'
        #
        # if a == b:
        #     return f'{minus * 1}'
        #
        # if b == 1:
        #     return f'{minus * a}'
        #
        return f'{self.whole_number()[0]}{a}/{b}'


m1 = VulgarFractions(-2, 4)
m2 = VulgarFractions(3, 5)

print(m1-m2)
