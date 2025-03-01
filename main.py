import unittest

def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 'invalid'
    
    if a + b <= c or b + c <= a or a + c <= b:
        return 'invalid'
    
    if a == b == c:
        return 'equilateral'
    
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'right'
    
    if a == b or b == c or a == c:
        return 'isosceles'
    
    return 'scalene'

if __name__ == '__main__':
    unittest.main()