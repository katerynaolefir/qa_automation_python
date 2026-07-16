alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
    )
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
def formatted(number):
    return format(number, ",").replace(",", " ")

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
total_area = area_black_sea + area_azov_sea
# formatted = format(total_area, ",").replace(",", " ")
print(f"Чорне та Азовське моря разом займають площу, яка становить {formatted(total_area)} км2.")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_inventory = 375291
first_and_second_inventory = 250449
second_and_third_inventory = 222950

first_inventory = all_inventory - second_and_third_inventory
second_inventory = first_and_second_inventory - first_inventory
third_inventory = all_inventory - (first_inventory + second_inventory)

print(f"На першому складі розміщено {formatted(first_inventory)} товарів, на другому складі {formatted(second_inventory)} товарів та на третьому складі {formatted(third_inventory)} товарів.")
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month = 1179
months_count = 18
total_cost = months_count * one_month

print(f"Вартість комп’ютера складає {formatted(total_cost)} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"Залишок від ділення чисел, які вказані в задачі 07 складає: a){a}, b){b}, c){c}, d){d}, e){e}, f){f}")
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza = 274 * 4
medium_pizza = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3

total_price = large_pizza + medium_pizza + juice + cake + water

print(f"Для даного замовлення всього знадобиться {formatted(total_price)} грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photos = 232
one_page_photos = 8
all_page_photos = all_photos // one_page_photos

print(f"Ігорю знадобиться всього {all_page_photos} сторінок, щоб вклеїти всі фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_tank_capacity = 48

every_step = 100
every_step_liters = 9
total_step = distance // every_step

total_liters_for_trip = total_step * every_step_liters
stop_gas_station = total_liters_for_trip // fuel_tank_capacity - 1

print(f"Для подорожі із Харкова в Будапешт знадобиться {total_liters_for_trip} літрів бензину.")
print(f"Кожного разу заправляючи повний бак, родині необхідно заїхати на заправку під час подорожі із Харкова в Будапешт {stop_gas_station} разів.")


