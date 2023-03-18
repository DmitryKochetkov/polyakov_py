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
        
        result = None
        for i in range(n-6):
            for j in range(i+6, n):
                x = a[i] * a[j]
                if x % 2 == 1 and (result == None or x < result):
                    result = x

        if result == None:
            return -1
        
        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        window = [0] * 6
        result = None

        for i in range(6):
           window[i] = int(f.readline())

        m = None # минимальное нечетное, встреченное до окна
        result = None

        for i in range(6, n):
            x = int(f.readline())

            y = window.pop(0)
            if y % 2 == 1 and (m == None or y < m):
                m = y
            
            window.append(x)

        if result is None:
            return -1

        return result

def solve():
    paths = generate_paths(9)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem9(unittest.TestCase):
    def test_answer(self):
        assert solve().split() == get_correct_answer(27, 9).split()

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())

