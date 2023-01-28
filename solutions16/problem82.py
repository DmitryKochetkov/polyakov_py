
import unittest
from answers import get_correct_answer

def F(n):
    if n <= 70:
        return F(n+2) + 2 * F(3 * n) 
    else:
        return n-50

def solve():
    return F(40)

class Problem82(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 72)

if __name__ == '__main__':
    print(solve())