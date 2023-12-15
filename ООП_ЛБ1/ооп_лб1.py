import doctest


# TODO Написать 3 класса с документацией и аннотацией типов

class DOM:
    def __init__(self, floor: (int, float), s_area: float):
        """
        Создание и подготовка к работе объекта "Дом"

        :param floor: Высота
        :param s_area: Площадь дома
        :raised TypeError: Когда аргументы - нечисловые типы данных
        :raised ValueError: Когда значение площади/высоты меньше или равно нулю

        Пример:
        >>> dom = DOM(800, 1.5) # инициализация экземпляра класса
        """

        if not isinstance(floor, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if floor <= 0:
            raise ValueError("Некорректное значение высоты")
        self.floor = floor

        if not isinstance(s_area, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if s_area <= 0:
            raise ValueError("Некорректное значение площади")
        self.s_area = s_area

    def increase_floor(self, add: int) -> None:
        """
        Метод увеличивает высоту дома

        :param add: Значение добавляемой высоты
        :raised TypeError: Только целочисленный тип
        :raised ValueError: Данный параметр увеличивает высоту, поэтому не может быть отрицательным

        Пример:
        >>> dom = DOM(800, 1.5)
        >>> dom.increase_floor(300)
        """
        if not isinstance(add, (int, float)):
            raise TypeError("Недопустимый тип данных")

        if add < 0:
            raise ValueError("Недопустимое значение")
        ...

    def change_slope(self) -> None:
        """
        Метод изменяет угол наклона крыши

        :raised TypeError: Если аргумент нечисловой тип данных

        Пример:
        >>> dom = DOM(800, 1.5)
        >>> dom.change_slope()
        """
        ...


class Room:
    def __init__(self, length: (int, float), width: (int, float)):
        """
        Создание и подготовка к работе объекта "Комната"

        :param length: Длина
        :param width: Ширина
        :raised TypeError: Когда аргументы - нечисловые типы данных
        :raised ValueError: Когда значение меньше или равно нулю

        Пример:
        >>> room = Room(3, 1.5) # инициализация экземпляра класса "Комната"
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if length <= 0:
            raise ValueError("Некорректное значение длины")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if width <= 0:
            raise ValueError("Некорректное значение ширины")
        self.width = width

    def square(self) -> None:
        """
        Метод для вычисления площади.

        :return: Возвращает площадь

        Пример:
        >>> room = Room(4, 2)
        >>> room.square()
        """

    def perimeter(self) -> None:
        """
        Метод для вычисления периметра

        :return: Возвращает периметр

        Пример:
        >>> room = Room(4, 2)
        >>> room.perimeter()
        """


class Circle:
    def __init__(self, radius: (int, float)):
        """
        Инициализация объекта "Круг"

        :param radius: Радиус
        :raised TypeError: Когда радиус - нечисловой типы данных
        :raised ValueError: Когда значение радиуса меньше или равно нулю

        Пример:
        >>> circle = Circle(5)
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if radius <= 0:
            raise ValueError("Некорректное значение радиуса")
        self.radius = radius

    def square(self):
        """
        Метод для вычисления
        площади круга
        Для реализации понадобиться импортировать модуль math(в частности math.pi)

        :return: Возвращает площадь круга

        Пример:
        >>> circle = Circle(5)
        >>> circle.square()
        """

    def length(self):
        """Метод для вычисления
        длины окружности.
        Для реализации понадобиться импортировать модуль math(в частности math.pi)

        :return: Возвращает длину окружности

        Пример:
        >>> circle = Circle(5)
        >>> circle.length()
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
