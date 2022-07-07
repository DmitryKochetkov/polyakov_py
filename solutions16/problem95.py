import unittest
from answers import get_correct_answer

def F(n):
    if n < 10:
        return n
    else:
        return F(G(n))

def G(n):
    if n < 10:
        return n
    else:
        a = n % 10 + G(n // 10)
        return a

def solve():
    return F(12345678987654321)

class Problem95(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 95)

if __name__ == '__main__':
    print(solve())