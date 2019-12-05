import division_master as div
from division_master import is_Number_Prime
from test_branch_01 import test_function_is_Number_Prime
from test_branch_01 import test_function_print_All_Divisors
from test_branch_01 import test_function_the_Biggest_Prime_Divisor
from test_branch_01 import test_function_the_Biggest_Devisor
from test_branch_01 import test_function_prime_Multipliers_Canonical

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
print('Число: {}.'.format(10), div.print_All_Divisors(10))
print('Число: {}.'.format(-10), div.print_All_Divisors(-10))
print()
print("Задание 3. Самый большой простой делитель числа.")
print('Число: {}.'.format(n), div.the_Biggest_Prime_Divisor(n))
print('Число: {}.'.format(z), div.the_Biggest_Prime_Divisor(z))
print('Число: {}.'.format(10), div.the_Biggest_Prime_Divisor(10))
print('Число: {}.'.format(777), div.the_Biggest_Prime_Divisor(777))
print('Число: {}.'.format(8984), div.the_Biggest_Prime_Divisor(8984))
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
print('Число: {}.'.format(78393), 'делитель: ', div.the_Biggest_Devisor('78393'))
print()
print()

# ТЕСТЫ
print('01. Тест функции is_Number_Prime:')
test_function_is_Number_Prime()
print()
print('02. Тест функции print_All_Divisors:')
test_function_print_All_Divisors()
print()
print('03. Тест функции the_Biggest_Prime_Divisor')
test_function_the_Biggest_Prime_Divisor()
print()
print('04. Тест функции the_Biggest_Devisor')
test_function_the_Biggest_Devisor()
print()
print('05. Тест функции prime_Multipliers_Canonical')
test_function_prime_Multipliers_Canonical()