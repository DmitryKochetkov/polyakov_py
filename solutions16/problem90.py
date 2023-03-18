import unittest
from answers import get_correct_answer

def F(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return F(n // 2) + 1
    return F(n-1) + n

def solve():
    for n in range(1, 1000):
        if F(n) == 19:
            return n

class Problem90(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 90)

if __name__ == '__main__':
    print(solve())