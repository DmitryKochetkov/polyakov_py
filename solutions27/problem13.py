import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer

def bruteforce(path: str):
    with open(path) as f:
        n = int(f.readline())
        a = list()

        for i in range(n):
            a.append(int(f.readline()))
        
        answer = 0
        for i in range(n):
            for j in range(i+7, n):
                if (a[i] * a[j]) % 14 == 0:
                    answer += 1

        return answer

def efficient(path: str):
    with open(path) as f:
        n = int(f.readline())
        buf = [int(f.readline()) for i in range(7)]
        answer = 0
        c14 = 0 # количество чисел, кратных 14, с индексами от 0 до i-7
        c2 = 0 # количество чисел, кратных 2, с индексами от 0 до i-7
        c7 = 0 # количество чисел, кратных 7, с индексами от 0 до i-7
        c = 0 # количество чисел, не кратных 2 и 7, с индексами от 0 до i-7

        for i in range(7, n):
            x = int(f.readline())
            if buf[i % 7] % 14 == 0:
                c14 += 1
            elif buf[i % 7] % 2 == 0:
                c2 += 1
            elif buf[i % 7] % 7 == 0:
                c7 += 1
            else:
                c += 1

            buf[i % 7] = x

            if x % 14 == 0:
                answer += c14 + c7 + c2 + c
            elif x % 2 == 0:
                answer += c14 + c7
            elif x % 7 == 0:
                answer += c14 + c2
            else:
                answer += c14
        
        return answer

def solve():
    paths = generate_paths(13)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem7(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 13)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, positive_numbers)

if __name__ == '__main__':
    print(solve())