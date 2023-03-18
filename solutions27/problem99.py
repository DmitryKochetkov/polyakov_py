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
            data.append(int(f.readline()))

        result_cost = 10 ** 20
        result_point = None

        for point in range(n):
            # print('Trying to build factory at {} with mass {}'.format(point, data[point]))
            cost = 0

            for j in range(n):
                distance = min(abs(j - point), abs(n - abs(j - point)))
                cost += data[j] * distance

            # print('\t Cost equals', cost)
            if cost < result_cost:
                result_cost = cost
                result_point = point

        return result_point + 1

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        a = [int(x) for x in f]
        k, d, s_t = n // 2 + 1, n % 2, sum(a)

        s = sum([a[i] * abs(i) for i in range(k - n, k)])
        s_m, L, p = s, sum(a[k:]), -1
        for i in range(n):
            z = a[k - n + i]
            s += 2 * (a[i] + L) - s_t - z * d
            L -= z - a[i]
            if s < s_m:
                p = i
                s_m = s
        return p+2

def solve():
    paths = generate_paths(99)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem99(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 99)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())