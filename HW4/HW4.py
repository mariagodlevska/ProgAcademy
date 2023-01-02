# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі
# - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири
# номер під'їзду, поверху та номер на поверсі. Якщо такої квартира немає в цьому будинку,
# то необхідно повідомити користувача про це.
# ( не використовувати if )

flat = int(input('flat= '))
n_floor = 9
n_onfloor = 4
n_block = 4

pidizd=(flat-1)//n_floor*n_onfloor+1
poverh=((flat-1)%(n_floor*n_onfloor))//n_onfloor+1
na_poversi=(flat+n_onfloor)%n_onfloor

(flat>(n_floor*n_onfloor*n_block) or flat<0) and print ('wrong number') or flat<=(n_floor*n_onfloor*n_block) \
and print (f'pidizd is {pidizd}', f'poverh is {poverh}', f'na poversi is {na_poversi}', sep='\n')

#2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є високосним, якщо він кратний 4,
# але не кратний 100, а також якщо він кратний 400

year = int(input('year= '))

(year%4 and (not year%100) or year%400) and print (year*365+1) or (not year%4) and print (year*365)

# #3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої. Дано: A, B, C - сторони трикутника.
# # Напишіть програму, яка вказує чи існує такий трикутник.

a=input('A= ')
b=input('B= ')
c=input('C= ')

if (a+b)>c and (c+b)>a and (a+c)>b:
    print('There is such a triangle.')

else:
    print('There is no such triangle.')