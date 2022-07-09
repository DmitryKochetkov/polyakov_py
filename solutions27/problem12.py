import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer

def bruteforce(path: str):
    with open(path) as f:
        n = int(f.readline())
        a = list()

        for i in range(n):
            a.append(int(f.readline()))

        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if (a[i] * a[j]) % 6 == 0:
                    answer += 1

        return answer

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        answer = 0
        k6 = 0 # количество кратных 6
        k3 = 0 # количество не кратных 6, кратных 3
        k2 = 0 # количество не кратных 6, кратных 2

        for i in range(n):
            x = int(f.readline())
            if x % 6 == 0:
                k6 += 1
            elif x % 3 == 0:
                k3 += 1
            elif x % 2 == 0:
                k2 += 1
        
        answer = k2 * k3 + k6 * (n - k6) + (k6 * (k6-1) // 2)
        return answer

def solve():
    paths = generate_paths(12)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem12(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 12)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())