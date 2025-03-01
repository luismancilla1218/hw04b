# test_main.py
import unittest
from main import classify_triangle

class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), 'equilateral')
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), 'isosceles')
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'scalene')
    
    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
    
    def test_invalid(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'invalid')
        self.assertEqual(classify_triangle(1, 1, 3), 'invalid')

if __name__ == '__main__':
    unittest.main()