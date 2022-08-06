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
                if s % 25 == 0:
                    result = max(result, s)

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        result = [0] * 25 # result[j] - максимальная сумма подпоследовательностей, в которых сумма элементов дает остаток j при делении на 25 к очередной итерации 

        for i in range(n):
            x = int(f.readline())
            resultNew = result.copy()

            for j in range(25):
                if result[j] != 0:
                    resultNew[(x + j) % 25] = max(resultNew[(x + j) % 25], result[j] + x)

            resultNew[x % 25] = max(resultNew[x % 25], x)
            result = resultNew.copy()
        
        return result[0]

def solve():
    paths = generate_paths(60)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem60(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 60)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())