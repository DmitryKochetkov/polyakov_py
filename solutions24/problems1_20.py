import unittest
from answers import get_correct_answer
from .utils import get_file_path

def solve(s):
    answer = 0
    a = 0

    for i in range(len(s)):    
        if s[i] == 'C':
            a += 1
        else:
            answer = max(answer, a)
            a = 0

    answer = max(answer, a)

    return answer

class Problems1_20(unittest.TestCase):
    def test(self):
        for i in range(1, 21):
            with open(get_file_path(i)) as f:
                assert int(solve(f.read())) == int(get_correct_answer(24, i)), 'Expected {}, actual {}'.format(get_correct_answer(24, i), solve(f.read()))

if __name__ == '__main__':
    print('Not implemented yet.')