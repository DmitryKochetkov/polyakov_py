from itertools import *
import unittest
from answers import get_correct_answer

def check_number(number):
    for i in range(len(number)-1):
        if number[i] % 2 == number[i+1] % 2:
            return False
    
    return True

def solve():
    answer = 0
    digits = range(8)

    for number in permutations(digits):
        if check_number(number):
            answer += 1

    print(answer)
    return answer

class Problem163(unittest.TestCase):
    def test(self):
        print(get_correct_answer(8, 163))
        assert str(solve()) == get_correct_answer(8, 163)

if __name__ == '__main__':
    print(solve())