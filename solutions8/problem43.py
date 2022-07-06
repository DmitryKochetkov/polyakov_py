from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    alphabet = ['Л', 'Е', 'Т', 'О']
    answer = 0
    for word in product(alphabet, repeat=5):
        if 'Е' in word:
            answer += 1
    return answer

class Problem43(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 43)

if __name__ == '__main__':
    print(solve())