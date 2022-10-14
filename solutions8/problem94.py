from itertools import *
import unittest
from answers import get_correct_answer

def check_word(word):
    if word[0] == 'Ь':
        return False
    
    return 'ЕЬ' not in ''.join(word)

def solve():
    answer = 0

    for word in permutations('ПАНЕЛЬ'):
        if check_word(word):
            answer += 1

    return answer

class Problem94(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 94)

if __name__ == '__main__':
    print(solve())