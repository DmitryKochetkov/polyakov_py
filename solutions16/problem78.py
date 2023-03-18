import unittest
from answers import get_correct_answer



class Problem78(unittest.TestCase):
    def test(self):
        assert str(solve()) == get_correct_answer(16, 78)

if __name__ == '__main__':
    print(solve())