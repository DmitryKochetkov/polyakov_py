import unittest
from answers import get_correct_answer

with open('./data/26data/26-k1.txt') as f:
    n, k = map(int, f.readline().split())
    prices = list()
    for i in range(n):
        prices.append(int(f.readline()))

    prices.sort()

    s = sum(prices[n-k : n])

    answer = '{} {}'.format(prices[n-k-1], int(s * 0.2))

class Problem21(unittest.TestCase):
    def test(self):
        expected = get_correct_answer(26, 21)
        assert answer == expected, f'Actual: {answer}, expected: {expected}'

if __name__ == '__main__':
    print(answer)

