import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer

from math import ceil


def bruteforce(path):
    with open(path) as f:
        n, capacity = map(int, f.readline().split())
        a = list()
        for line in f.readlines():
            x, p = map(int, line.split())
            a.append((x, ceil(p / capacity))) # Заменяем p на p со звездочкой

        a.sort(key = lambda x: x[0])

        min_cost = 10 ** 10
        optimal_start = 1

        for i in range(n): # проходимся по способам выбрать пункт для лаборатории
            start = a[i][0]
            cost = 0

            for j in range(n):
                if j != i:
                    x, p = a[j]
                    cost += abs(x - start) * p
            
            if cost < min_cost:
                min_cost = cost
                optimal_start = start

        return min_cost

def efficient(path):
    with open(path) as f:
        n, capacity = map(int, f.readline().split())
        a = list()
        for line in f.readlines():
            x, p = map(int, line.split())
            a.append((x, ceil(p / capacity))) # Заменяем p на p со звездочкой

        a.sort(key = lambda x: x[0])

        # Считаем стоимость при условии, что лаборатория установлена в первом пункте
        cost = 0
        start = a[0][0]
        ps = [0] * n # префикс-сумма по p
        ps[0] = a[0][1]
        # Считаем начальную стоимость
        for i in range(n):
            x, p = a[i]
            cost += abs(x - start) * p

        for i in range(1, n):
            ps[i] = ps[i-1] + a[i][1]

        min_cost = cost
        optimal_start = 0

        for i in range(1, n):
            cost = cost + (a[i][0] - a[i-1][0]) * (ps[i-1] - ps[n-1] + ps[i-1])
            # print(cost)
            if cost < min_cost:
                min_cost = cost
                optimal_start = i

        return min_cost

def solve():
    paths = generate_paths(122)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

def generate_tubes(path):
    with open(path, 'w+') as f:
        n = 15
        capacity = 36
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 10000)) + '\n')


class Problem122(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 122)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())