list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
print(f"Сумма усіх парних чисел в лісті: {sum(even_numbers)}")