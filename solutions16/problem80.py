from itertools import *
import unittest
from answers import get_correct_answer

def F(n):
    try:
        if n <= 5:
            return (True, n)
        elif n % 3 == 0:
            x = F(n // 3 + 2)
            if x[0]:
                return (True, n + x[1])
            else:
                return (False, 0)
        else:
            x = F(n+3)
            if x[0]:
                return (True, n + x[1])
            else:
                return (False, 0)
    except RecursionError:
        return (False, 0)

def solve():
    n = 6
    k = F(n)
    while True:
        n += 1
        k = F(n)
        if k[0] and k[1] >= 1000:
            break

    return n

class Problem80(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 80)

if __name__ == '__main__':
    print(solve())