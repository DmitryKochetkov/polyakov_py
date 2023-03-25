import unittest
from answers import get_correct_answer

with open('./data/26data/26-k3.txt') as f:
    n, k, m = map(int, f.readline().split())
    a = list(map(int, f.readlines()))
    a.sort(reverse=True)
    # min_prise_score = min(a[k:(k+m)])
    # min_winner_score = min(a[:k])
    min_prise_score = a[k+m-1]
    min_winner_score = a[k-1]

class Problem23(unittest.TestCase):
    def test(self):
        actual = [min_prise_score, min_winner_score]
        expected = list(map(int, get_correct_answer(26, 23).split()))
        assert actual == expected, f'Actual: {actual}, expected: {expected}'

if __name__ == '__main__':
    print(min_prise_score, min_winner_score)
