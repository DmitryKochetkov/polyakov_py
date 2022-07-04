import unittest
from .utils import *
from .utils.data import *
from answers import answers27

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
                if x % 7 == 0 and x % 49 != 0 and x > result:
                    result = x

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())
        m7 = 0
        m = 0

        for i in range(n):
            x = int(f.readline())
            if x % 7 == 0 and x % 49 != 0 and x > m7:
                m7 = x
            elif x % 7 != 0 and x > m:
                m = x

        return m7 * m

def solve():
    paths = generate_paths(7)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem7(unittest.TestCase):
    def test_problem7(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)
        assert solve() == answers27[7]

if __name__ == '__main__':
    print(solve())