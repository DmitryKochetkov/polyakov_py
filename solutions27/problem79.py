import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from collections import defaultdict

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()

        for i in range(n):
            a.append(int(f.readline()))

        answer = 0
        for i in range(n):
            for j in range(i, n):
                if a[i] % 21 == 0 and a[i] == a[j] * a[j]:
                    answer = max(answer, j-i+1)

        return answer

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        m = defaultdict(lambda: None)

        answer = 0
        for i in range(n):
            x = int(f.readline())
            if x % 21 == 0 and m[x] == None:
                m[x] = i

            if m[x ** 2] != None:
                answer = max(answer, i - m[x ** 2] + 1)

        return answer

def solve():
    paths = generate_paths(79)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem79(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 79)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())