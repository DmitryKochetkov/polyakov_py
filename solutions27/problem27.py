import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            a.append(pair)

        result = 0

        # option - кортеж вида (i, x), где i - номер пары, x - 0 или 1, индекс элемента пары, который выбран в сумму
        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if hex(s)[-1] != 'a':
                result = max(result, s)

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())

        s = 0
        m = 10**20
        for i in range(n):
            x, y = map(int, f.readline().split())
            s += max(x, y)
            d = abs(x-y)
            if abs(x-y) % 16 != 0:
                m = min(m, abs(d))

        # Шестнадцатеричная запись s оканчивается на a, тогда и только тогда, когда s % 16 == 10, так как hex(10) = A
        if hex(s)[-1] != 'a':
            return s
        else:
            return s - m

def solve():
    paths = generate_paths(27)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem27(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 27)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())