import unittest
from answers import get_correct_answer

def F(n):
    if n <= 5:
        return n
    elif n > 5 and n % 5 == 0:
        return n + F(n / 5 + 1)
    elif n > 5 and n % 5 != 0:
        return n + F(n+6)

def solve():
    m = 0
    n = 8
    while n < 200:
        if n % 6 != 0:
            if F(n) > 1000:
                m = n
                break
            n += 1
        else:
            n += 2
    
    return m

class Problem81(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 81)

if __name__ == '__main__':
    print(solve())