import unittest
from answers import get_correct_answer

def F(n):
    if n < 0:
        raise ValueError()
    if n <= 2 or n == 8:
        return 0
    if n == 3:
        return 1
    return F(n-2) + F(n-1)

def solve():
    for n in range(100):
        if F(n) == 25:
            return n

class Problem109(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 109)

if __name__ == '__main__':
    print(solve())