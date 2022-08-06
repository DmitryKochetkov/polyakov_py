import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import combinations

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        data = list()
        result = 0

        for i in range(n):
            x = int(f.readline())
            data.append(x)

        for i in range(1, n+1):
            for option in combinations(data, i):
                s = sum(option)
                if s % 3 == 0:
                    result += 1

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        result = [0, 0, 0] # result[j] - количество подпоследовательностей, в которых сумма элементов дает остаток j при делении на 2 к очередной итерации 

        for i in range(n):
            x = int(f.readline())
            resultNew = result.copy()

            for j in range(3):
                resultNew[(x + j) % 3] += result[j]

            resultNew[x % 3] += 1
            result = resultNew.copy()
        
        return result[0]

def solve():
    paths = generate_paths(58)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem58(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 58)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())