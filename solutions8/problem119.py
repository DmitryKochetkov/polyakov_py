import unittest
from answers import get_correct_answer
from itertools import permutations

def check_word(word) -> bool:
    """
    Проверяет, подходит ли это слово в этой задаче.
    """
    n_vowels = 0
    for letter in word:
        if letter in 'АИ':
            n_vowels += 1

    return n_vowels <= 1

def solve():
    result = 0
    alphabet = 'МАГИСТР'
    for word in permutations(alphabet, 5):
        if check_word(word):
            result += 1

    return result

class Problem119(unittest.TestCase):
    def test_answer(self):
        assert str(solve()) == get_correct_answer(8, 119)

if __name__ == '__main__':
    print(solve())