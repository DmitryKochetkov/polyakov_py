import unittest
from answers import get_correct_answer
from math import sqrt, floor, ceil

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

answer = []
a = 113000000
b = 114000000
for i in range(ceil(sqrt(a // 2)), ceil(sqrt(b // 2))):
    if is_prime(i):
        answer.append([2*i*i, i])

class Problem148(unittest.TestCase):
    def test(self):
        assert [' '.join([str(x) for x in item]) for item in answer] == get_correct_answer(25, 148).split('\n')

if __name__ == '__main__':
    for item in [' '.join([str(x) for x in item]) for item in answer]:
        print(item)

