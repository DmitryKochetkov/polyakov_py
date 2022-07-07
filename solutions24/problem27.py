import unittest
from answers import get_correct_answer
from .utils import get_file_path

def solve():
    with open(get_file_path(27)) as f:
        s = f.read()
        pattern = 'EAB'

        answer = 0
        a = 0

        for i in range(len(s)):    
            if s[i] == pattern[a % 3]:
                a += 1
            else:
                answer = max(answer, a)
                a = 0

        answer = max(answer, a)

        return answer

class Problem27(unittest.TestCase):
    def test(self):
        assert int(solve()) == int(get_correct_answer(24, 27))

if __name__ == '__main__':
    print(solve())