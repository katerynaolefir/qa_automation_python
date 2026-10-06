
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:

            yield num



print('Парні числа')
for num in even_numbers(5):
    print(num)