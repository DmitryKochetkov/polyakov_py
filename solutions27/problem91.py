import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from itertools import product

def isSpecial(x):
    if x >= 0:
        return False

    x = abs(x)
    
    s = 0
    while x > 0:
        s += x % 3
        x //= 3

    return s == 12

def input_generator91(path):
    with open(path, 'w+') as f:
        n = 15
        k = randint(1, 6)
        d = randint(1, 6)
        f.write(str(n) + ' ' + str(k) + ' ' + str(d) + '\n')

        for i in range(n):
            f.write(str(randint(-100000, 100000)) + '\n')

def bruteforce(path):
    with open(path) as f:
        n, k, d = map(int, f.readline().split())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))

        result = -10001
        for length in [x * d for x in range(1, n // d + 1)]:
            for l in range(n-length+1):
                r = l+length
                s = sum(a[l:r])
                c = 0
                for x in a[l:r]:
                    if isSpecial(x):
                        c += 1

                if c % k == 0 and s > result:
                    result = s

        return result

def efficient(path):
    with open(path) as f:
        n, k, d = map(int, f.readline().split())
        answer = -10001
        s = 0
        count = 0

        infty = 10 ** 20
        m = [infty] * k # m[i] - минимальная префикс-сумма, в которой количество особенных кратно k
        c = [0] * k # c[i] - номер итерации, на которой встречена префикс-сумма m[i]

        for i in range(n):
            x = int(f.readline())
            s += x

            if isSpecial(x):
                count += 1

            r = count % k

            if s > answer and r == 0 and i % d == 0:
                answer = s
            elif m[r] != infty and s - m[r] > answer and c[r] % d == i % d:
                answer = s - m[r]
            
            if s < m[r]:
                m[r] = s
                c[r] = i

        return answer

def solve():
    paths = generate_paths(91)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem91(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 91)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, input_generator91, verbose=True)

if __name__ == '__main__':
    print(solve())