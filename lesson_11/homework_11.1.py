array = ['1,2,3,4, 2.6', '1,2,3,4,50', 'qwerty1,2,3']

def type_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)

def sum_of_numbers(string_of_num):
    numbers = string_of_num.split(',')
    return sum(type_number(n) for n in numbers)

for item in array:
    try:
        print(sum_of_numbers(item), end=', ')
    except ValueError:
        print('Не можу це зробити!', end='')
