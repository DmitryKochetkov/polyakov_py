import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        s_max = 0
        a = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            s_max += max(pair)
            a.append(pair)

        result = None

        # option - кортеж вида (i, x), где i - номер пары, x - 0 или 1, индекс элемента пары, который выбран в сумму
        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if (s % 10) == s_max % 10 and (result == None or s < result):
                result = s

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        data = list()
        s_max = 0
        
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            s_max += max(pair)
            data.append(pair)

        s = 0
        infty = 10 ** 20
        m = infty

        dMin = [10 ** 20] * 10

        for x, y in data:
            s += min(x, y)
            d = abs(y - x)
            r = d % 10

            if r > 0:
                dMinNew = dMin[:]
                for k in range(1, 10):
                    r0 = (r + k) % 10
                    dMinNew[r0] = min(d + dMin[k], dMinNew[r0])

                dMinNew[r] = min(d, dMinNew[r])
                dMin = dMinNew[:]

        if s % 10 == s_max % 10:
            return s
        else:

            return s + dMin[(s_max % 10 - s % 10)]

def solve():
    paths = generate_paths(47)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem47(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 47)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())