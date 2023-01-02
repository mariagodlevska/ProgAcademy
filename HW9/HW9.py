# 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.

# def conc(a, b, text):
#     return f'{int(a)+int(b)}{text}'
#
# print(conc(a= input(), b = input() , text = input()))

# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». Її параметрами будуть цілі числа,
# які описують довжину та ширину такого прямокутника.

# def rectangle(h, w):
#     return f"{w * '*'}\n" + \
#            f"*{(w - 2) * ' '}* \n" * (h-2) + \
#            f"{w * '*'}"
#
# print (rectangle(int(input('Height=')), int(input('Width='))))

# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
#
# def finding_element (elements, x):
#     for index, i in enumerate(elements):
#         if x==i:
#             return index
#
#     return -1
#
#
# print(finding_element(input('elements'), input('Target number: ')))

# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.

# def word_counter(txt):
#     return len(txt.split())
#
#
# print(word_counter(input()))

# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents


# def textified_numbers(number):
#     text_numbers_d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#                       10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
#                       16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
#                       40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred',
#                       1_000: 'thousand', 1_000_000: 'million', 1_000_000_000: 'billion'}
#
#     x = 1
#     a = int(number % 100)
#     test = int((number // x) % 1000 % 100)
#     b = int(test % 10)
#     c = int(test // 10 *10)
#     d = int((number // x) % 1000 // 100)
#     cents = round(((number % 1) * 100))
#     text = ['$', 'cent(s)']
#
#     if (cents * 100) // x < 20:
#         text.insert(1, text_numbers_d.get(cents))
#
#     elif (cents // x) >= 20:
#         text.insert(1, text_numbers_d.get(cents % 10))
#         text.insert(1, text_numbers_d.get((cents // 10)*10))
#
#     while number / x >= 1:
#         if x == 1:
#             pass
#         else:
#             text.insert(0, text_numbers_d.get(x))
#
#         if number > 100:
#             if (number // x) % 100 < 20:
#                 text.insert(0, text_numbers_d.get(a))
#
#             elif (number // x) % 100 >= 20:
#                 text.insert(0, text_numbers_d.get(b))
#                 text.insert(0, text_numbers_d.get(c))
#
#             if number // x >= 100:
#                 text.insert(0, text_numbers_d.get(100))
#                 text.insert(0, text_numbers_d.get(d))
#
#         else:
#             if (number // x) < 20:
#                 text.insert(0, text_numbers_d.get(number))
#
#             elif (number // x) >= 20:
#                 text.insert(0, text_numbers_d.get(b))
#                 text.insert(0, text_numbers_d.get(c))
#
#             if number // x >= 100:
#                 text.insert(0, text_numbers_d.get(100))
#                 text.insert(0, text_numbers_d.get(d))
#
#         x = x * 1000
#         test = int((number // x) % 1000 % 100)
#         b = int(test % 10)
#         c = int(test // 10 *10)
#         d = int((number // x) % 1000 // 100)
#
#     return ' '.join(text)
#
#
# print('text number: ', textified_numbers(float(input('Number: '))))
#
# # 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# # Наприклад: XXII -> 22
# # Докладніше: https://en.wikipedia.org/wiki/Roman_numerals

def roman_numerals_converter(roman_number):
    roman_number_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    arabic_number = 0
    u = 'MCMXIX'

    for letter in range(len(roman_number)-1):
        if roman_number_d.get(f'{roman_number[letter]}') < roman_number_d.get(f'{roman_number[letter + 1]}'):
            arabic_number -= roman_number_d.get(f'{roman_number[letter]}')

        else:
            arabic_number += roman_number_d.get(roman_number[letter])

    arabic_number += roman_number_d.get(f'{roman_number[letter + 1]}')

    return arabic_number

print('arabic number: ', roman_numerals_converter(input('roman number: ')))
