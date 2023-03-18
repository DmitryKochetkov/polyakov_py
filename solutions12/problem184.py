import unittest
from answers import get_correct_answer

answer = '7' * 170
while '777' in answer:
    answer = answer.replace('77', '2', 1)
    answer = answer.replace('22', '7', 1)

class Problem184(unittest.TestCase):
    def test(self):

        assert str(answer) == get_correct_answer(12, 184)

if __name__ == '__main__':
    print(answer)