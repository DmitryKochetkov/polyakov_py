import unittest
from answers import get_correct_answer

with open('./data/26data/26-k2.txt') as f:
    n, k = map(int, f.readline().split())
    measures = list()

    for i in range(n):
        measures.append(int(f.readline()))

    measures.sort()
    
    measures = measures[k : -k]
    avg = sum(measures) / len(measures)
    answer = '{} {}'.format(max(measures), int(avg))

class Problem22(unittest.TestCase):
    def test(self):
        expected = get_correct_answer(26, 22)
        assert answer == expected, f'Actual: {answer}, expected: {expected}'

if __name__ == '__main__':
    print(answer)

