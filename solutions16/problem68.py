import unittest
from answers import get_correct_answer

def F(n):
    if n < 3:
        return n + 1
    elif n % 2 == 0:
        return F(n-2) + n-2
    else:
        return None
        return F(n+2) + n+2

def solve():
    c = 0
    for i in range(1, 1000):
        result = F(i)
        if result is not None and len(str(result)) == 5:
            c += 1

    return c

class Problem68(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 68)

if __name__ == '__main__':
    for i in range(1, 1000):
        print(f"F({i}) = {F(i)}")
    print(solve())