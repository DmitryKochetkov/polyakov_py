from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    alphabet = ['К', 'А', 'Т', 'Е', 'Р']
    answer = 0
    for word in product(alphabet, repeat=4):
        if word.count('Р') >= 2:
            answer += 1
    
    return answer

class Problem50(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 50)

if __name__ == '__main__':
    print(solve())