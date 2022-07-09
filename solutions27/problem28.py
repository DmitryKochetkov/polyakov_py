import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product, combinations

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            a.append(pair)

        result = None

        # option - кортеж вида (i, x), где i - номер пары, x - 0 или 1, индекс элемента пары, который выбран в сумму
        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if (s % 8) != 2 and (result == None or s < result):
                result = s

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        s = 0
        infty = 10 ** 20
        m = infty

        for _ in range(n):
            x, y = map(int, f.readline().split())
            if x > y:
                x, y = y, x
            
            s += x
            d = y - x
            
            if d % 8 != 0:
                m = min(m, d)

        if (s % 8) != 2:
            return s
    
        return s + m

def solve():
    paths = generate_paths(28)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem28(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 28)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())