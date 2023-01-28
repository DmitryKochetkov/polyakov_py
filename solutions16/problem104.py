import unittest
from answers import get_correct_answer

from math import floor

def F(n):
    if n == 0:
        return 1
    if n <= 10:
        return F(n-1)
    if n < 100:
        return 2.2 * F(n-3)
    return 1.7 * F(n-2)

def solve():
    x = floor(F(40))
    result = 0
    for digit in str(x):
        result += int(digit)
    return result

class Problem104(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 104)

if __name__ == '__main__':
    print(solve())