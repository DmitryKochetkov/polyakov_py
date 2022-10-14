from itertools import *
import unittest
from answers import get_correct_answer

def check_word(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return False

    return True

def solve():
    answer = 0

    for word in set(permutations('АБАК')):
        if check_word(word):
            answer += 1

    return answer

class Problem114(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 114)

if __name__ == '__main__':
    print(solve())