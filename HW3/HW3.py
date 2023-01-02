# 1. Write a Python program to print the number entered by user only if the number entered is negative.

x = float(input('Number = '))

x>0 or print (x)

# 2. Write a Python program to check if the value a is less than 20 or not.

y = float(input('Number = '))

print (f'Is {y} >20?', y>20, sep='\n')

# 3. Write a Python program to check if a given number is Zero or Not.

z = float(input('Number = '))

print (f'Is {z} zero?', z==0, sep='\n')

# 4. Write a Python program to check if a given number is Even or Odd.

a = int(input('Number = '))

print (f'Is {a} odd?', a % 2==1, sep='\n')

# 5. Write a Python program to find largest number among three numbers
# entered by user.

print ('Enter 3 numbers = ')
b1 = input ('1. ')
b2 = input ('2. ')
b3 = input ('3. ')

biggest = [b1,b2,b3]

print (max(biggest))
