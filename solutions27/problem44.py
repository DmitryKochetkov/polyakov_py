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
        for option in product(permutations([0, 1, 2]), repeat = n):
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

            if len(odds) == 3:
                result = max(result, max(odds))
            elif len(odds) == 2:
                result = max(result, max(evens))

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        s = [0, 0, 0]
        
        infty = 10 ** 20
        dMin1 = infty
        dMin2 = infty

        for _ in range(n):
            triplet = list(map(int, f.readline().split()))
            triplet.sort()

            for j in range(3):
                s[j] += triplet[j]

            for j in range(2):
                d = triplet[2] - triplet[j]
                if d % 2 == 1:
                    if d < dMin1:
                        dMin2 = dMin1
                        dMin1 = d
                    elif d < dMin2:
                        dMin2 = d
            
        if s[0] % 2 == 1 and s[1] % 2 == 1:
            return s[2]

        result = s[2]
        # if dMin1 == infty:
        #     return 0

        if s[0] % 2 == 0:
            result -= dMin1

        if s[1] % 2 == 0:
            result -= dMin2

        return result

def solve():
    paths = generate_paths(44)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem44(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 44)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_triplets)

if __name__ == '__main__':
    print(solve())