"""
Модуль содержит классы для представления геометрических фигур
"""

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# - Доработайте класс прямоугольник из прошлых семинаров.
# - Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых
# значений (отрицательных).
# - Используйте декораторы свойств.
from my_utils6.my_exceptions import MyValueError


class Range:
    """
    Клас-дескриптор для контроля границ значения переменной
    """
    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        """
        Устанавливаем защищенный параметр
        :param owner:
        :param name:
        :return:
        """
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError(f'Значение {value} должно быть числом')
        if self.min_value is not None and value < self.min_value:
            raise MyValueError(f'Значение {value} должно быть больше {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise MyValueError(f'Значение {value} должно быть меньше {self.max_value}')


class MyRectangle:
    """
    Класс прямоугольник, который может быть квадратом
    """
    width = Range(min_value=0)
    height = Range(min_value=0)

    def __init__(self, *args):
        if len(args) == 1:  # Если один параметр - то это квадрат
            self.width = args[0]
            self.height = args[0]
        else:
            self.width = args[0]
            self.height = args[1]

    def rectangle_len(self):
        """
        Периметр прямоугольника
        :return:
        """
        return 2 * (self.height + self.width)

    def rectangle_square(self):
        """
        Площадь прямоугольника
        :return:
        """
        return self.height * self.width

    def __add__(self, other):
        """
        Сложение двух прямоугольников
        :param other:
        :return:
        """
        new_width = self.width + other.width
        new_height = self.height + other.height
        return MyRectangle(new_width, new_height)

    def __sub__(self, other):
        """
        Вычитание прямоугольников
        :param other:
        :return:
        """
        new_width = self.width - other.width
        new_height = self.height - other.height
        return MyRectangle(new_width, new_height)

    def __eq__(self, other):
        """
        Равенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() == other.rectangle_square()

    def __ne__(self, other):
        """
        Неравенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return not self == other

    def __gt__(self, other):  # >
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() > other.rectangle_square()

    def __lt__(self, other):  # <
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() < other.rectangle_square()

    def __ge__(self, other):  # <=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() <= other.rectangle_square()

    def __le__(self, other):  # >=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() >= other.rectangle_square()

    def __repr__(self):
        """
        Представление объекта для программистов
        :return:
        """
        return f'({self.width=}, {self.height=})'

    def __str__(self):
        """
        Представление объекта для пользователей
        :return:
        """
        return f'Прямоугольник {self.width} x {self.height}'
