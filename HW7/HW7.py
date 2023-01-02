# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.

b='b'

print (input ('text: ').count(b))

# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність
# (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери,
# за якою повинні йти маленькі).

n = input ('name: ')

m = not n.isnumeric() and not n.isalnum() and n.istitle() and 'valid name' or 'Name is not valid'

print(m)

# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.

phrase = input ('type here: ')

p=0
for i in phrase:
    p+= ord(i)

print(p)

# 4. Виведіть на екран 10 рядків із значенням числа Pi.
# У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.

import math

for i in range(2, 12):
    print(f'{math.pi:.{i}f}')

# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.

import string

txt = input ('type here: ')

for i in string.punctuation:
    while i in txt:
        txt= txt.replace(i, '')

txt= txt.split()

print (max(txt, key=len))

# Додаткові задачі до домашнього завдання:
# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"

txt = input ('type here: ')
l=len(txt)


for i in range(1, len(txt)//2+1):
    if len(txt[:i])*txt.count(txt[:i]) == l:
        print(txt[:i])
        break

# 2. Напишіть програму для очищення тексту від HTML-тегів.
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації.
# Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">

html= '<div class="about"> \
                <h2 class="about-position">Shinobi of Konohagakure\'s Hatake clan<h/2> \
                <h1 class="about-name">Kakashi Hatake</h1> \
                <p class="about-description">I have no desire to tell you my likes and dislikes…</p> </div> '

while '<' in html:
    html = html.replace(html[html.find('<'):html.find('>')+1], '')

while '   ' in html:
    html = html.replace('   ', '  ')

html = html.replace('\n ', '').strip()
html = html.replace('  ', '\n')
print(html)