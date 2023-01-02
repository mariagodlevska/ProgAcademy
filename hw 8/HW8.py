# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".

days = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6: 'Sat', 7:'Sun'}

for k, v in days.items():
    print(k, v)

p = int(input('number='))
print(p, days.get(p))

# 2. Опишіть кота (домашня тварина) на основі словника.

cat = {'name:': 'Iza', 'breed': 'turkish angora', 'fur:': 'long', 'color:': 'White', 'age:': 0.5, 'character:': 'playful'}

for k, v in cat.items():
    print(k, v)

# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.

inp = input('Write here:')

d = {}
for i in inp:
    if i.isalpha():
        d[i] = inp.count(i)

print (d)

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку.
# Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».

a, b = set(input('a:')), set(input('b:'))

s = a&b

print(s)

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.

n=100

c_number=3
d_number=5

c, d, e = set(), set(), set()

for i in range(c_number, n):
    if not i%c_number:
        c.add(i)

for j in range(d_number, n):
    if not j%d_number:
        d.add(j)

print(c, d, sep='\n')

# 6. Створіть список із числами, які є в обох списках.

e = c&d

print (e)


