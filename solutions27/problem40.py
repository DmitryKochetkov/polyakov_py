import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product, permutations

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for _ in range(n):
            triplet = list(map(int, f.readline().split()))
            a.append(triplet)

        result = 0

        # option - список кортежей размера n кортежей размера 3 вида (i1, i2, i3)
        for option in tqdm(product(permutations([0, 1, 2]), repeat = n), total=6 ** n):
            s = [0, 0, 0]
            for i, x in enumerate(option):
                s[0] += a[i][x[0]]
                s[1] += a[i][x[1]]
                s[2] += a[i][x[2]]

            odds = []
            evens = []

            for item in s:
                if item % 2 == 0:
                    evens.append(item)
                else:
                    odds.append(item)

            if len(odds) > 1 and len(evens) > 0:
                result = max(result, max(odds))
            elif len(evens) > 1 and len(odds) > 0:
                result = max(result, max(evens))

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        s = [0, 0, 0]
        
        infty = 10 ** 20
        dMin = infty

        for _ in range(n):
            triplet = list(map(int, f.readline().split()))
            triplet.sort()

            for j in range(3):
                s[j] += triplet[j]

            for j in range(2):
                d = triplet[2] - triplet[j]
                if d % 2 == 1:
                    dMin = min(dMin, d)
            
        if s[0] % 2 != s[1] % 2:
            return s[2]

        if dMin < infty:
            return s[2] - dMin

        return 0

def solve():
    paths = generate_paths(40)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem40(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 40)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_triplets)

if __name__ == '__main__':
    print(solve())
    # test_with_bruteforce(bruteforce, efficient, positive_triplets, verbose=True)