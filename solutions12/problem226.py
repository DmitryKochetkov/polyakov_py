import unittest
from answers import get_correct_answer
from itertools import permutations

# for i in range(1, 5)

# 2x + 3 * 10 + 7z = 82

answer = '3' * 10
while '23' in answer:
    answer = answer.replace('23', '7', 1)

class Problem226(unittest.TestCase):
    def test(self):

        assert str(answer) == get_correct_answer(12, 226)

if __name__ == '__main__':
    print(answer)