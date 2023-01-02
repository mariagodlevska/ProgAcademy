# Домашнє завдання:
# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

import string
import math

number_list = str(input('Your numbers: '))

for i in string.punctuation:
    number_list = number_list.replace(i, ' ')

number_list = number_list.replace(string.punctuation, ' ')

number_list = list(map(int, number_list.split(' ')))


def func_seq(number_list):
    if arithmetic_prog(number_list):
        return number_list[-1] + arithmetic_prog(number_list)
    elif geometric_prog(number_list):
        return number_list[-1] * geometric_prog(number_list)
    elif power_prog(number_list):
        return power_prog(number_list)[1] ** power_prog(number_list)[0]
    else:
        return 'Sequence is incorrect'


def arithmetic_prog(number_list: list):
    d = number_list[1] - number_list[0]
    for x in range(len(number_list)-1):
        if (number_list[x+1] - number_list[x]) != d:
            return False

    return d


def geometric_prog(number_list: list):
    d = number_list[1] / number_list[0]
    for x in range(len(number_list)-1):
        if (number_list[x+1] / number_list[x]) != d:
            return False

    return d


def power_prog(number_list: list):
    for x in range(2, len(number_list)):
        lo = round_half_up(math.log((number_list[x]), (x+1)), 3)
        if round_half_up(math.log((number_list[x-1]), x), 3) != \
                round_half_up(math.log((number_list[x]), (x+1)), 3):
            return False

    return lo, (x+2)


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


print(func_seq(number_list))



# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множинами яких чисел він є.

# pal_list = []
# pal_ab_list = []
# for a in range (100, 1000):
#     for b in range (100, 1000):
#         if str(a*b) == str(a*b)[::-1]:
#             pal_list.append(a*b)
#             pal_ab_list.append(f'{a}*{b} =')
#         else:
#             b += 1
#
# d = pal_list.index(max(pal_list))
# print(pal_ab_list[d], max(pal_list))
