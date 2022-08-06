import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path: str):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            a.append(pair)

        result = None

        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if s % 5 == 0 and (result == None or s < result):
                result = s

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        s = 0
        m = [10 ** 20] * 5

        for i in range(n):
            x, y = map(int, f.readline().split())
            d = abs(x-y)
            s += min(x,y)

            r = d % 5

            if r > 0:
                m2 = m.copy()
                for k in range(1, 5):
                    r0 = (r + k) % 5
                    m2[r0] = min(m2[r0], m[k] + d)
                m2[r] = min(m2[r], d)
                
                m = m2.copy()

        if s % 5 == 0:
            return s

        return s + m[5 - s % 5]

def solve():
    paths = generate_paths(5)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem5(unittest.TestCase):
    def test_answer(self):
        assert solve().split() == get_correct_answer(27, 5).split()

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())

