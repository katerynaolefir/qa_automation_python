"""Функція, яка обчислює суму двох чисел. """
def sum_of_numbers(a, b):
    return a + b

"""  Функція, яка розрахує середнє арифметичне списку чисел."""
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

"""  Функція, яка приймає рядок та повертає його у зворотному порядку. """
def reversed_string(text):
    return text[::-1]

"""  Функція, яка приймає список слів та повертає найдовше слово у списку."""
def the_longest_word(words):
    return max(words, key=len)

"""  Функція, яка індекс першого входження str2 у str1, або -1, якщо не знайдено."""
def find_substring(str1, str2):
    return str1.find(str2)