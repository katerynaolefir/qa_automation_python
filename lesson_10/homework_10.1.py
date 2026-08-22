from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return round(math.pi * self.__radius ** 2, 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.__radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return round(self.__width * self.__height, 2)

    def get_perimeter(self):
        return round((self.__width + self.__height) * 2, 2)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.__base = base
        self.__height = height
        self.__side1 = side1
        self.__side2 = side2

    def get_area(self):
        return round((self.__base * self.__height) / 2, 2)

    def get_perimeter(self):
        return round(self.__base + self.__side1 + self.__side2, 2)


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(6, 4, 5, 5)
]

for shape in shapes:
    print(f"площа = {shape.get_area()}, периметр = {shape.get_perimeter()}")