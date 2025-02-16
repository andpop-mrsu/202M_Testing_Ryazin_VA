import unittest

from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangleFunction(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(1, 1, 1), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(7, 7, 5), "isosceles")

    def test_scalene(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_invalid_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 5, 0)

    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, -6)


if __name__ == "__main__":
    unittest.main()
