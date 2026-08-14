class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, (int, float)):
                raise TypeError('Сторона повинна бути числом')
            if value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError('Сторона повинна бути більше 0')

        elif key == 'angle_a':
            if not isinstance(value, (int, float)):
                raise TypeError('Кут повинен бути числом')
            if 0 < value < 180:
                super().__setattr__(key, value)
                super().__setattr__('angle_b', 180 - value)
            else:
                raise ValueError('Кут повинен бути від 0 до 180')

        else:
            super().__setattr__(key, value)



figure = Rhombus(5, 60)
print(f"Сторона ромба: {figure.side_a}, Кут А: {figure.angle_a}, Кут Б: {figure.angle_b}")
