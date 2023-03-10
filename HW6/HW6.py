# 1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.

for i in range (7,101,7):
    print(i)

#'if not i%x' is the same as 'if i%x==0'

#print([i for i in range(1, 101) if not i % 7])

# 2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).

factorial = int(input('number='))
i=1
x=1

if factorial<0:
    print ("Negative numbers don't have factorials")
else:
    while i<factorial:
        x=(factorial-i)*x
        i+=1
    print (f'factorial for {factorial} is {x}')

# 3. Написати Python-скрипт, який виводить на екран таблицю множення на 5.
# Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...

n=5

for i in range (1,11):
    print(f'{i}*{n}={i*n}')

# 4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
# Висота і ширина прямокутника вводяться з клавіатури.
# Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.
# *****
# *   *
# *   *
# *****

h, w = int(input('Height=')), int(input('Width='))

print ((w+2)*'*')

for i in range (1,h-1):
    print ('*', (w-2)*' ','*')

print ((w+2)*'*')

# 5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому.

p=[0,5,2,4,7,1,3,19]
sum=0

for i in range (len(p)):
     if p[i]%2:
         sum=sum+1
print (sum)

# 6. Створіть список випадкових чисел (розміром 4 елементи).
# Створіть другий список у два рази більше першого, де перші 4 елементи повинні дорівнювати елементам першого списку,
# а решта елементів - подвоєним значенням початкових.
# Наприклад,
# Було → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]

import random

list1 = []

for i in range (0, 4):
    list1.append(random.randint (1, 100))

print(list1)

for i in range (0, 4):
    list1.append(list1[i]*2)

print(list1)


# 7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

salary=[]

for i in range (12):
    salary.append(float(input(f'salary {i+1}= ')))

o=sum(salary)/len(salary)

print (salary, f'The average salary is {o}.', sep='\n')

# 8. Є матриця
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]
# [13, 14, 15, 16]
# Напишіть Python-скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.

m = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]

k=0

for i in m:
    print('\t'.join(map(str, i)))
    k += sum(i)

print(f'Sum of matrix is {k}')

# 9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.

l = [7,2,9,4,5]

print(l, '-->', list(reversed(l)))

# 10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.

for n in range(3,101):
    for i in range (2,n):
        if not n%i:
            break
    else:
        print(n)

# 11. Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне).
# У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****

c=int(input('n='))

if not c%2:
    print ('must be odd')
else:
    for i in range(c, 0, -2):
        print (' '*((c-i)//2), i*'*')
    for i in range(3, c + 1, 2):
        print (((c-i)//2)*' ', i*'*')