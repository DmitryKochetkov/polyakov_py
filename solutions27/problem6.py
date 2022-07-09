import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path: str):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))
        
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                x = a[i] * a[j]
                if x % 6 == 0 and x > result:
                    result = x

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        m = 0
        m2 = 0
        m3 = 0
        m61 = 0
        m62 = 0

        for i in range(n):
            x = int(f.readline())
            if x % 6 == 0:
                if x > m61:
                    m62 = m61
                    m61 = x
                elif x > m62:
                    m62 = x
            elif x % 3 == 0:
                m3 = max(m3, x)
            elif x % 2 == 0:
                m2 = max(m2, x)
            else:
                m = max(m, x)

        return max(m2 * m3, max(m2, m3, m) * m61, m61 * m62)

def solve():
    paths = generate_paths(6)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem6(unittest.TestCase):
    def test_answer(self):
        assert solve().split() == get_correct_answer(27, 6).split()

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())

