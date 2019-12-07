from division_master import is_Number_Prime
from division_master import print_All_Divisors
from division_master import the_Biggest_Prime_Divisor
from division_master import the_Biggest_Devisor
from division_master import prime_Multipliers_Canonical

# 22 теста
# is_Number_Prime
def test_01_is_Number_Prime():
    assert is_Number_Prime(571) == True

def test_02_is_Number_Prime():
    assert is_Number_Prime(379) == True

def test_03_is_Number_Prime():
    assert is_Number_Prime(967) == True

def test_04_is_Number_Prime():
    assert is_Number_Prime(682) == False

def test_05_is_Number_Prime():
    assert is_Number_Prime(985) == False

def test_06_is_Number_Prime():
    assert is_Number_Prime(1009) == 'Функция принимает на вход числа от 1 до 1000'

#print_All_Divisors

def test_01_print_All_Divisors():
    assert print_All_Divisors(765) == [1, 3, 5, 9, 15, 17, 45, 51, 85, 153, 255, 765]

def test_02_print_All_Divisors(): # пропущено одно число, тест должен быть failed
    assert print_All_Divisors('765') == [1, 3, 5, 9, 15, 17, 45, 51, 85, 153, 255, 765]

def test_03_print_All_Divisors():
    assert print_All_Divisors(982) == [1, 2, 491, 982]

def test_04_print_All_Divisors():
    assert print_All_Divisors(349) == [1, 349]

def test_05_print_All_Divisors():
    assert print_All_Divisors(16782) == [1, 2, 3, 6, 2797, 5594, 8391, 16782]

# the_Biggest_Prime_Divisor
def test_01_the_Biggest_Prime_Divisor():
    assert the_Biggest_Prime_Divisor(546) == 13

def test_02_the_Biggest_Prime_Divisor():
    assert the_Biggest_Prime_Divisor(394) == 197

def test_03_the_Biggest_Prime_Divisor():
    assert the_Biggest_Devisor(94) == 47

def test_04_the_Biggest_Prime_Divisor():
    assert the_Biggest_Devisor('9672') == 4836

def test_05_the_Biggest_Prime_Divisor():
    assert the_Biggest_Devisor(197.742625) == 'Функция принимает на вход целые числа'

#prime_Multipliers_Canonical
def test_01_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(6) == [(2, 1), (3, 1)]

def test_02_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(56) == [(2, 3), (7, 1)]

def test_03_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(853) == 'Вы ввели простое число' # простые числа определяет только до 1000

def test_04_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(7651) == [(7, 1), (1093, 1)]

def test_05_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(9973) == [] #на входе простое число

def test_06_prime_Multipliers_Canonical():
    assert prime_Multipliers_Canonical(9975) == [(3, 1), (5, 2), (7, 1), (19, 1)]
