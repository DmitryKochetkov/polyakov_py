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
            triplet = list(map(int, f.readline().split()))
            a.append(triplet)

        result = 0
        
        for option in list(product([0, 1, 2], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if s % 8 == 0 and s > result:
                result = s

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())
        s = 0

        dMin = [10 ** 20] * 8
        for _ in range(n):
            triplet = list(map(int, f.readline().split()))
            triplet.sort()
            s += triplet[2]

            dMinNew = dMin.copy()
            for i in range(0, 2):
                d = triplet[2] - triplet[i]
                r = d % 8

                if r > 0:
                    for k in range(1, 8):
                        r0 = (r + k) % 8
                        dMinNew[r0] = min(dMinNew[r0], dMin[k] + d)

                    dMinNew[r] = min(dMinNew[r], d)
            dMin = dMinNew.copy()
        
        if s % 8 == 0:
            return s

        return s - dMin[s % 8]

def solve():
    paths = generate_paths(11)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem11(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 11)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_triplets)

if __name__ == '__main__':
    print(solve())