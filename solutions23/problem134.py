import unittest
from answers import get_correct_answer

def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return f(start-1, end) + f(start // 2, end)

x = int('110111', 2)
y = int('110', 2)

answer = f(x, y)

class Problem134(unittest.TestCase):
    def test(self):
        assert answer == get_correct_answer(23, 134)

if __name__ == '__main__':
    print(answer)
