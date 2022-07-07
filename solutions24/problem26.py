import unittest
from answers import get_correct_answer
from .utils import get_file_path

def solve():
    with open(get_file_path(26)) as f:
        s = f.read()
        vowels = 'AE'
        answer = 0
        b = 0
        for i in range(len(s)):
            if s[i] not in vowels:
                b += 1
                if answer < b:
                    answer = b
            else:
                b = 0
        return answer

class Problem26(unittest.TestCase):
    def test(self):
        assert int(solve()) == int(get_correct_answer(24, 26))

if __name__ == '__main__':
    print(solve())