import unittest
from answers import get_correct_answer
from itertools import permutations

def check_word(word) -> bool:
    """
    Проверяет, подходит ли это слово в этой задаче.
    """
    if word[0] == 'Ь':
        return False

    for i in range(len(word)-1):
        if word[i+1] in 'ЕАР' and word[i] == 'Ь':
            return False

    return True

def solve():
    result = 0
    alphabet = 'ПЕСКАРЬ'
    for word in permutations(alphabet):
        if check_word(word):
            result += 1

    return result

class Problem113(unittest.TestCase):
    def test_answer(self):
        assert str(solve()) == get_correct_answer(8, 113)

if __name__ == '__main__':
    print(solve())