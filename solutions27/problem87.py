import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer

def isSpecial(x):
    if x >= 0:
        return False

    x = abs(x)
    
    while x > 0:
        if x % 5 == 2:
            return False
        x //= 5

    return True

def input_generator87(path):
    with open(path, 'w+') as f:
        n = 10
        k = randint(1, 15)
        f.write(str(n) + ' ' + str(k) + '\n')

        for i in range(n):
            f.write(str(randint(1, 10000)) + '\n')

def bruteforce(path):
    with open(path) as f:
        n, k = map(int, f.readline().split())
        a = list()
        for i in range(n):
            a.append(int(f.readline()))

        result = -10001
        # for length in range(1, n+1):
        #     for l in range(n-length+1):
        for l in range(n):
            for r in range(l, n):
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
        n, k = map(int, f.readline().split())
        answer = 0
        count = 0 # количество особенных
        s = 0 # сумма всех чисел

        infty = 10 ** 20
        m = [infty] * k # m[i] - минимальная префикс-сумма, в которой количество особенных кратно k

        for _ in range(n):
            x = int(f.readline())
            s += x

            if isSpecial(x):
                count += 1

            r = count % k

            if r == 0 and s > answer:
                answer = max(answer, s)
            elif m[r] != infty and s - m[r] > answer:
                answer = s - m[r]

            m[r] = min(m[r], s)
        
        return answer

def solve():
    paths = generate_paths(87)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem87(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 87)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, input_generator87)

if __name__ == '__main__':
    print(solve())