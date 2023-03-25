import unittest
from answers import get_correct_answer


with open('./data/26data/26-j1.txt') as f:
    a = list()

    n = int(f.readline())
    for i in range(n):
        x = int(f.readline())
        a.append(x)

    res = 0
    for i in range(n):
        for j in range(i):
            if a[i] + a[j] == 100:
                res += 1
                a[i] = 0
                a[j] = 0


class Problem26(unittest.TestCase):
    def test(self):
        expected = get_correct_answer(26, 26)
        assert res == expected, f'Actual: {res}, expected: {expected}'

if __name__ == '__main__':
    print(res)
