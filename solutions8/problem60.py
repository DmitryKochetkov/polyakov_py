from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    alphabet_middle = ['А', 'Б', 'В', 'Г']
    alphabet_first_and_last = ['Э', 'Ю', 'Я']
    answer = 0

    def check_word(word):
        if word[0] not in alphabet_first_and_last:
            return False
        
        if word[-1] not in alphabet_first_and_last:
            return False
        
        return all([letter in alphabet_middle for letter in word[1:-1]])

    for word in product(alphabet_middle + alphabet_first_and_last, repeat=5):
        if check_word(word):
            answer += 1

    return answer

class Problem60(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(8, 60)

if __name__ == '__main__':
    print(solve())