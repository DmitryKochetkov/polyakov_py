from itertools import *
import unittest
from answers import get_correct_answer

# Плохая функция
def F(n):
    if n < -100000:
        return 1
    elif n > 10:
        return F(n-1) + 3*F(n-3)+2
    else:
        return -F(n-1)

# Хорошая эквивалентная функция
def G(n):
    if n <= 10:
        if n % 2 == 1:
            return 1
        else:
            return -1
    else:
        return G(n-1) + 3*G(n-3)+2

def solve():
    return G(20)

class Problem74(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 74)

if __name__ == '__main__':
    print(solve())