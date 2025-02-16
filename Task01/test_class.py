import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral_triangle():
    triangle = Triangle(1, 1, 1)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 3

def test_isosceles_triangle():
    triangle = Triangle(7, 7, 5)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 19

def test_scalene_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 5, 0)

def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 4, -5)


if __name__ == "__main__":
    pytest.main()