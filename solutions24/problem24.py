import unittest
from answers import get_correct_answer
from .utils import get_file_path

def solve():
    with open(get_file_path(24)) as f:
        s = f.read()
        answer = 0
        a = 0

        for i in range(len(s)):    
            if s[i] != 'D':
                a += 1
            else:
                answer = max(answer, a)
                a = 0

        answer = max(answer, a)

        return answer

class Problem24(unittest.TestCase):
    def test(self):
        assert int(solve()) == int(get_correct_answer(24, 24))

if __name__ == '__main__':
    print(solve())