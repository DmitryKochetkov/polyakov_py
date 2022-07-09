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

        for option in list(product([0, 1], repeat=n)):
            s = 0
            for i, x in enumerate(option):
                s += a[i][x]

            if s % 3 == 0 and (result == None or s > result):
                result = s

        return result

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())

        # Очевидно, наша цель - брать все время наибольшее число из пары.

        r11 = 100001
        r12 = 100001
        r21 = 100001
        r22 = 100001

        s = 0 # ответ на задачу

        for _ in range(n):
            x, y = map(int, f.readline().split())
            if x > y:
                x, y = y, x

            # теперь x - меньшее из чисел, y - большее

            s += y

            d = y - x
            
            if d % 3 == 1:
                if d < r11:
                    r12 = r11
                    r11 = d
                elif (d < r12):
                    r12 = d
            
            elif d % 3 == 2:
                if d < r21:
                    r22 = r21
                    r21 = d
                elif d < r22:
                    r22 = d

        if s % 3 == 0:
            return s
        elif s % 3 == 1:
            return max(s - r11, s - r21 - r22)
        else:
            return max(s - r21, s - r11 - r12)

def solve():
    paths = generate_paths(2)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem2(unittest.TestCase):
    def test_answer(self):
        assert solve().split() == get_correct_answer(27, 2).split()

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_pairs)

if __name__ == '__main__':
    print(solve())

