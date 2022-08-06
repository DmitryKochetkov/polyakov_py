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

        result = -10001
        for length in range(1, n+1):
            for l in range(n-length+1):
                r = l+length
                
                c5 = 0
                c7 = 0
                for x in a[l:r]:
                    if x % 5 == 0:
                        c5 += 1
                    if x % 7 == 0:
                        c7 += 1

                if c5 == c7 and length > result:
                    result = length

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        answer = 0
        
        c = 0 # префикс-счетчик на i-й итерации
        c5 = 0 # количество кратных 5 на i-й итерации
        c7 = 0 # количество кратных 7 на i-й итерации

        d = {} # d[j] - минимальная сумма среди подпоследовательностей, в которой разность между c5 и c7 равна j
        
        for i in range(n):
            x = int(f.readline())
            c += 1

            if x % 5 == 0:
                c5 += 1
            if x % 7 == 0:
                c7 += 1

            if c5 == c7:
                answer = max(c, answer)
            elif c5 - c7 not in d:
                d[c5 - c7] = c
            else:
                answer = max(c - d[c5 - c7], answer)
                d[c5 - c7] = min(d[c5 - c7], c)
        
        return answer

def solve():
    paths = generate_paths(94)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem94(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 94)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())