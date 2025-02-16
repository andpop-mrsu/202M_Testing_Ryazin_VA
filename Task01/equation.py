import math


def find_roots(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен 0, так как уравнение не является квадратным.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "Нет вещественных корней"
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])