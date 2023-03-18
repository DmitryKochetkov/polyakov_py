import unittest
from answers import get_correct_answer

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start == 33:
        return 0
    else:
        x = start
        while x == start or not is_prime(x):
            x += 1
        return f(start + 2, end) + f(x, end)

def solve():
    return f(2, 14) * f(14, 45)

class Problem125(unittest.TestCase):
    def test(self):
        assert solve() == get_correct_answer(23, 125)

if __name__ == '__main__':
    print(solve())