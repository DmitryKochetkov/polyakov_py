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
        for l in range(n):
            for r in range(l+1, n):
                if a[l] > 0 and a[r] > 0 and (a[l] + a[r]) % 2 == 0 and 0 in a[l+1:r]:
                    answer += 1

        return answer

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        z = -1 # позиция ближайшего слева нуля к i-му элементу
        c1 = 0 # количество положительных нечетных элементов до текущего z-го
        c2 = 0 # количество положительных четных элементов до текущего z-го

        r1 = 0
        r2 = 0
        answer = 0

        for i in range(n):
            x = int(f.readline())
            if x == 0:
                z = i
                c1 += r1
                c2 += r2
                r1 = 0
                r2 = 0
            elif x > 0:
                if x % 2 == 0:
                    answer += c2
                    r2 += 1
                else:
                    answer += c1
                    r1 += 1

        return answer

def solve():
    paths = generate_paths(35)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem35(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 35)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())