
def fibonacci_numbers(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b




for num in fibonacci_numbers(50):
    print(f'Число: {num}')