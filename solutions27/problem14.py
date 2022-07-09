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
                if (a[i] + a[j]) % 12 == 0:
                    answer += 1

        return answer

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        answer = 0
        r = [0] * 12
        for i in range(n):
            x = int(f.readline())
            r[x % 12] += 1

        answer += r[0] * (r[0] - 1) // 2
        answer += r[6] * (r[6] - 1) // 2

        for i in range(1, 6):
            answer += r[i] * r[12-i]
        return answer

def solve():
    paths = generate_paths(14)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem14(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 14)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())