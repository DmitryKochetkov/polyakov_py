import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        data = list()

        for i in range(n):
            triplet = list(map(int, f.readline().split()))
            data.append(triplet)

        result = 10 ** 20
        for option in product([0, 1, 2], repeat=n):
            s = 0
            for i in range(n):
                s += data[i][option[i]]
            
            if s % 7 != 0:
                result = min(result, s)

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        s = 0
        dMin = 10 ** 20

        for i in range(n):
            triplet = list(map(int, f.readline().split()))
            triplet.sort()

            s += triplet[0]
            for j in [1, 2]:
                d = triplet[j] - triplet[0]
                r = d % 7
                if r != 0:
                    dMin = min(dMin, d)
    
        if s % 7 != 0:
            return s
        else:
            return s + dMin

def solve():
    paths = generate_paths(30)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem30(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 30)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_triplets)

if __name__ == '__main__':
    print(solve())