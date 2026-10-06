def handle_exceptions(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            print(f"Не можна ділити на нуль")
        except TypeError:
            print("Неправильний тип даних")

    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b


print(divide(10, 2))
print(divide("10", 0))
print(divide(10, 0))