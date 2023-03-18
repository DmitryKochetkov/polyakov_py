import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def isSpecial(x):
    return x > 0 and x % 2 == 0

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))

        result = -10001
        for length in range(1, n+1):
            for l in range(n-length+1):
                r = l+length
                s = 0
                c = 0
                for x in a[l:r]:
                    s += x
                    if isSpecial(x):
                        c += 1

                if c == 1 and s > result:
                    result = s

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        answer = 0
        count = 0 # количество особенных
        s = 0 # сумма всех чисел (текущая префикс-сумма на i-й итерации)

        infty = 10 ** 20
        m = infty # минимальная префикс-сумма, в которой count-1 особенных чисел
        m_next = infty # минимальная префикс-сумма, в которой count особенных чисел

        for i in range(n):
            x = int(f.readline())
            s += x

            if isSpecial(x):
                count += 1
                m = m_next
                m_next = infty

            if count == 1 and s > answer:
                answer = max(answer, s)
            elif count > 1:
                answer = max(answer, s - m)
                m_next = min(m_next, s)
        
        return answer

def solve():
    paths = generate_paths(92)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem92(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 92)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers, verbose=True)

if __name__ == '__main__':
    print(solve())