import unittest
from .utils import *
from .utils.data import *
from answers import get_correct_answer
from random import randint

def isPrime(x: int):
    if x == 1:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    
    return True

def input_generator82(path):
    with open(path, 'w+') as f:
        n = 15
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 10000)) + '\n')

def bruteforce(path):
    with open(path) as f:
        n = int(f.readline())
        k = 9
        a = list()
        for i in range(n):
            a.append(int(f.readline()))

        result = 0
        for length in range(1, n+1):
            for l in range(n-length+1):
                c = 0
                s = sum(a[l:l+length])
                for i in range(l, l+length):
                    # s += a[i]
                    if isPrime(a[i]):
                        c += 1

                if c % k == 0 and s > result:
                    result = s

        return result

def efficient(path):
    with open(path) as f:
        n = int(f.readline())
        k = 9
        
        count = 0 # количество простых чисел
        s = 0 # сумма всех чисел (на i-й итерации это i-ая префикс-сумма)
        infty = 10 ** 20
        tailSum = [0] + [infty] * (k-1) # tailSum[j] - наименьшее значение префикс-суммы, в которой количество простых чисел дает остаток j при делении на k
        answer = 0

        for i in range(n):
            x = int(f.readline())
            s += x
            if isPrime(x):
                count += 1
            
            r = count % k
            # if tailSum[r] is None:
            #     tailSum[r] = s # такое заполнение обеспечивает, что tailSum[r] - наименьшая префикс-сумма, ведь префикс-суммы неубывают с увеличением индекса
            # elif count >= k:
            #     answer = max(answer, s - tailSum[r])

            if r == 0 and s > answer: # если r = 0, то подходит сама префикс-сумма
                answer = max(answer, s)
            elif tailSum[r] != infty and s - tailSum[r] > answer:
                answer = s - tailSum[r]


            tailSum[r] = min(tailSum[r], s)

        return answer

def solve():
    paths = generate_paths(82)
    solutions = {}

    for letter in ['A', 'B']:
        with open(paths[letter]) as f:
            solutions[letter] = efficient(paths[letter])

    return '{} {}'.format(*solutions.values())

class Problem82(unittest.TestCase):
    def test_answer(self):
        assert solve() == get_correct_answer(27, 82)

    def test_random(self):
        assert test_with_bruteforce(bruteforce, efficient, input_generator82)

if __name__ == '__main__':
    print(solve())