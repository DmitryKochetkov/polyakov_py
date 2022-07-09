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
        
        result = 10 ** 20
        for i in range(n):
            for j in range(i+5, n):
                x = (a[i] ** 2) + (a[j] ** 2)
                if x < result:
                    result = x

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())
        window = [0] * 5
        answer = 10 ** 20
        m = None

        for i in range(n):
            if i >= 5 and (m == None or window[i % 5] < m):
                m = window[i % 5]
            x = int(f.readline())
            window[i % 5] = x

            if m != None:
                answer = min(answer, m ** 2 + window[i % 5] ** 2)

        return answer

def solve():
    paths = generate_paths(8)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem8(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 8)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())