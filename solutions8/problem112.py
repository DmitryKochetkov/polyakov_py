import unittest
from answers import get_correct_answer
from itertools import permutations

def check_word(word) -> bool:
    """
    Проверяет, подходит ли это слово в этой задаче.
    """
    if word[-1] == 'Ь':
        return False

    for i in range(1, len(word)-1):
        if word[i-1] in 'ЕИ' and word[i+1] == 'ЕИ' and word[i] == 'Ь':
            return False

    if word[-1] == 'Ь' and word[-2] in 'ЕИ':
        return False

    if word[0] == 'Ь' and word[1] in 'ЕИ':
        return False

    return True

def solve():
    result = 0
    alphabet = 'ВЕНТИЛЬ'
    for word in permutations(alphabet):
        if check_word(word):
            result += 1

    return result

class Problem112(unittest.TestCase):
    def test_answer(self):
        assert str(solve()) == get_correct_answer(8, 112)

if __name__ == '__main__':
    print(solve())