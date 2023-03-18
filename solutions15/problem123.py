import unittest
from answers import get_correct_answer
from functools import lru_cache

def f(x, a):
    return x % 18 != 0 or (x % a == 0 or x % 12 != 0)

def check(a):
    for x in range(1, 1000):
        if not f(x, a):
            return False

    return True

answer = None
for a in range(1, 1000):
    if check(a):
        answer = a
        break

if __name__ == '__main__':
    print(answer)

class Problem123(unittest.TestCase):
    def test(self):
        answer = solve()

        assert str(answer[19]) == get_correct_answer(19, 11)
        assert str(answer[20]) == get_correct_answer(20, 11)
        assert ' '.join([str(i) for i in answer[21]]) == get_correct_answer(21, 11)

if __name__ == '__main__':
    print(solve())