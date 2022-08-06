import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        s_max = 0
        data = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            s_max += max(pair)
            data.append(pair)

        result = 0

        for option in list(product([0, 1], repeat=n)):
            s = 0
            c = [0, 0]

            for i, x in enumerate(option):
                s += data[i][x]
                c[data[i][x] % 2] += 1

            if s > result and (s % 2 != c.index(max(c))):
                result = s

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        c = [0, 0]
        result = 0
        m = 10 ** 20

        for i in range(n):
            x, y = sorted(list(map(int, f.readline().split())))
            c[y % 2] += 1
            d = y - x
            if d % 2 == 1:
                m = min(m, d)

            result += y

        if result % 2 != c.index(max(c)):
            return result
        
        return result - m

def solve():
    paths = generate_paths(50)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem50(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 50)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())