import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()

        for i in range(n):
            a.append(int(f.readline()))

        answer = 0
        for i in range(n):
            for j in range(i+2, n):
                if (a[i] + a[j]) % 3 == 0 and (sum(a[i+1:j]) % 2 == 0):
                    answer += 1

        return answer

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        c0 = [0] * 3 # c[j] - количество четных до i-1 итерации, дающих при делении на 3 остаток j
        c1 = [0] * 3 # c[j] - количество нечетных до i-1 итерации, дающих при делении на 3 остаток j

        x_prev = int(f.readline())
        answer = 0
        s = 0

        for i in range(1, n):
            x = int(f.readline())
            s += x_prev
            r = x % 3

            if s % 2 == 0:
                answer += c0[(3-r) % 3]
            else:
                answer += c1[(3-r) % 3]

            if s % 2 == 0:
                c0[x_prev % 3] += 1
            else:
                c1[x_prev % 3] += 1

            x_prev = x

        return answer

def solve():
    paths = generate_paths(76)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem76(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 76)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())