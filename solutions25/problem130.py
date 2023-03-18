import unittest
from answers import get_correct_answer
from math import sqrt, ceil, floor

def get_divisors(x):
    result = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            result.append(i)
            if i * i != x:
                result.append(x // i)
        
        if len(result) > 3:
            return []

        i += 1
    return result

a = ceil(sqrt(50034679))
b = floor(sqrt(92136895))

answer = []
for i in range(a, b+1):
    x = i ** 2
    d = get_divisors(x)
    if len(d) == 3:
        answer.append([x, max(d)])

class Problem130(unittest.TestCase):
    def test(self):
        assert [' '.join([str(x) for x in item]) for item in answer] == get_correct_answer(25, 130).split('\n')

if __name__ == '__main__':
    print([' '.join([str(x) for x in item]) for item in answer])

