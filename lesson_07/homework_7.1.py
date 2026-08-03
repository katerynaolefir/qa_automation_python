# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers(a, b):
    return a + b

print(f"Сума чисел: {sum_of_numbers(10, 14)}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Середнє арифметичне списку чисел: {average(numbers)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_string(text):
    return text[::-1]

line_for_reverse = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку."
print(f"Рядок у зворотному порядку: {reversed_string(line_for_reverse)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest_word(words):
    return max(words, key=len)

list_of_words = ["Написати", "функцію", "яка", "приймає", "список", "слів"]
print(f"Найдовше слово це {the_longest_word(list_of_words)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

# Задача з homework_6.4
"""Перевіряє, чи є число парним та сумує"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

result = list(filter(is_even, list_of_numbers))
print(f"Сумма усіх парних чисел в лісті: {sum(result)}")

# task 8
# Задача з homework_6.3
"""Створює новий рядок, який містить лише змінні типу стрінг, які присутні в lst1"""

def new_list_str(new_list):
    new_list = [i for i in new_list if isinstance(i, str)]
    return new_list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(f"Список, який містить лише змінні типу стрінг: {new_list_str(lst1)}")
# task 9

# Задача з homework_6.2
"""Запитує слово у користувача, поки в ньому не з'явиться літера 'h'"""

def check_letter(word):
    return "h" in word.lower()

enter_word = input('Введіть слово: ')

if check_letter(enter_word):
    print('Слово з літерою "h" введено')
else:
    print('Слово введено без літери "h"')


# task 10

# Задача з homework_6.1
"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False"""

def count_unique_symbols(text):
    return len(set(text)) > 10

text = input("Введіть строку: ")
print(count_unique_symbols(text))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""