import unittest
from answers import get_correct_answer

answer = 0
for n in range(1, 10000):
    s = bin(n)[2:]
    if s.count('1') > s.count('0'):
        s = s + '1'
    else:
        s = s + '0'
    
    result = int(s, 2)
    if result < 100 and result > answer:
        answer = result


class Problem194(unittest.TestCase):
    def test(self):

        assert str(answer) == get_correct_answer(5, 194)

if __name__ == '__main__':
    print(answer)