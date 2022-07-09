import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def bruteforce(path: str):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for _ in range(n):
            pair = list(map(int, f.readline().split()))
            a.append(pair)

        result = None

        # option - кортеж вида (i, x), где i - номер пары, x - 0 или 1, индекс элемента пары, который выбран в сумму
        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if s % 3 != 0 and (result == None or s < result):
                result = s

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        r1 = 100001 # минимальное из всех не взятых в сумму чисел, дающее в остатке от деление на 3 число 1
        r2 = 100001 # минимальное из всех не взятых чисел, дающее в остатке от деление на 3 число 2

        s = 0 # ответ на задачу

        for _ in range(n):
            x, y = map(int, f.readline().split())
            if x > y:
                x, y = y, x

            # теперь x - меньшее из чисел, y - большее

            s += x

            d = y - x
            if d < r1 and d % 3 == 1:
                r1 = d
            if d < r2 and d % 3 == 2:
                r2 = d

        if s % 3 != 0:
            return s
        
        return min(s + r1, s + r2)

def solve():
    paths = generate_paths(1)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem1(unittest.TestCase):
    def test_answer(self):
        assert solve().split() == get_correct_answer(27, 1).split()

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())

