class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам его сторон.
    
    :param a: длина первой стороны
    :param b: длина второй стороны
    :param c: длина третьей стороны
    :return: строка с типом треугольника ('equilateral', 'isosceles', 'nonequilateral')
    :raises IncorrectTriangleSides: если стороны не образуют треугольник
    
    Примеры:
    >>> get_triangle_type(1, 1, 1)
    'equilateral'
    >>> get_triangle_type(7, 7, 5)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны не образуют треугольник.
    >>> get_triangle_type(1, 5, 0)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны не образуют треугольник.
    >>> get_triangle_type(3, 4, -5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны не образуют треугольник.
    """
    if (a <= 0) or (b <= 0) or (c <= 0) or (a + b <= c or a + c <= b or b + c <= a):
        raise IncorrectTriangleSides("Стороны не образуют треугольник.")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
