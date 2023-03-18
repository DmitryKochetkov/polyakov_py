import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))
        
        optimal_sum = 0
        answer = 10 ** 20

        for l in range(n):
            for r in range(l+1, n):
                s = sum(a[l:r])
                length = r-l
                if s % 69 == 0:
                    if s > optimal_sum:
                        answer = length
                        optimal_sum = s
                    elif s == optimal_sum:
                        answer = min(answer, length)
        
        return answer

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        answer = 10 ** 20
        optimal_sum = 0
        s = 0

        sMin = [None] * 69 # sMin[k] - последняя наименьшая префикс-сумма, для которой s % 69 == k
        dMin = [None] * 69 # dMin[k] - номер итерации, на котором встречена sMin

        for i in range(n):
            x = int(f.readline())
            s += x

            if sMin[s % 69] != None:
                length = i - dMin[s % 69]
                current_sum = s - sMin[s % 69]

                if current_sum > optimal_sum:
                    answer = length
                    optimal_sum = current_sum
                elif current_sum == optimal_sum:
                    answer = min(answer, length)

            if sMin[s % 69] == None or s <= sMin[s % 69]:
                dMin[s % 69] = i
                sMin[s % 69] = s

        return answer

def solve():
    paths = generate_paths(71)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem71(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 71)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())