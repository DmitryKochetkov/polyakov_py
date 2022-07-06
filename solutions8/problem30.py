from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    return len(list(product(['Г', 'О', 'Д'], repeat=4))) * len(list(product(['Г', 'Д'], repeat=2)))

class Problem30(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 30)

if __name__ == '__main__':
    print(solve())