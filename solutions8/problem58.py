from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    consonants = ['П', 'Р', 'Г']
    vowels = ['И', 'О']
    alphabet = consonants + vowels

    def check_word(word):
        if word.count('О') > 2 or word[0] == 'О':
            return False

        for i in range(1, len(word)):
            if word[i] == 'О' and word[i-1] not in consonants:
                return False
        
        return True

    answer = 0
    for word in product(alphabet, repeat=4):
        if check_word(word):
            answer += 1
    
    return answer

class Problem58(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 58)

if __name__ == '__main__':
    print(solve())