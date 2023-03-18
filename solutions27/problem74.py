import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def input_generator74(path):
    with open(path, 'w+') as f:
        n = 100
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 100000)) + '\n')

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))
        
        answer = 0
        for l in range(n):
            for r in range(l+1, min(l+21, n)):
                if sum(a[l:r]) % 39 == 0:
                    answer += 1
        
        return answer

# def efficient(path):
#     with open(path) as f:
#         n = int(f.readline())
#         answer = 0

#         s = [int(f.readline())] # последние 20 префикс сумм
#         for i in range(1, 20):
#             s.append(s[i-1] + int(f.readline()))

#         for k in range(19):
#             if s[-1] % 39 == s[k] % 39:
#                 answer += 1

#         for i in range(n-20):
#             for k in range(19):
#                 if s[-1] % 39 == s[k] % 39:
#                     answer += 1
#             x = int(f.readline())
#             s.pop(0)
#             s.append(s[-1] + x)
        
#         return answer

def solve():
    paths = generate_paths(74)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = bruteforce(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem74(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 74)

    # def test_random(self):
    #     assert test_with_bruteforce(bruteforce, efficient, input_generator74, verbose=True)

if __name__ == '__main__':
    print(solve())