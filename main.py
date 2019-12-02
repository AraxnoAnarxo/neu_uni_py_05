import division_master as div
from division_master import is_Number_Prime

n = 1000
z = 273801
print()
print("Задание 1. Простое ли число?")
print('Число: {}.'.format(n), is_Number_Prime(n))
print('Число: {}.'.format(z), is_Number_Prime(z))
print('Число: {}.'.format(571), is_Number_Prime(571))
print()
print("Задание 2. Все делители числа.")
print('Число: {}.'.format(n), div.print_All_Divisors(n))
print('Число: {}.'.format(z), div.print_All_Divisors(z))
print()
print("Задание 3. Самый большой простой делитель числа.")
print('Число: {}.'.format(n), div.the_Biggest_Prime_Divisor(n))
print('Число: {}.'.format(z), div.the_Biggest_Prime_Divisor(z))
print()
print("Задание 4. Каноническое разложение числа на простые множители.")
print('Число: {}.'.format(n))
print(div.prime_Multipliers_Canonical(n))
print()
print('Число: {}.'.format(z))
print(div.prime_Multipliers_Canonical(z))
print()
print("Задание 5. Самый большой делитель числа (не обязательно простой).")
print('Число: {}.'.format(n), 'делитель: ', div.the_Biggest_Devisor(n))
print('Число: {}.'.format(z), 'делитель: ', div.the_Biggest_Devisor(z))