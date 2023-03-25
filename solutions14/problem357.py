import unittest
from answers import get_correct_answer

from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

v = {}
for x in alphabet[:15]:
    for y in alphabet[:17]:
        d = int("123" + x + "5", 15) + int("67" + y + "9", 17)
        if d % 131 == 0:
            v[y] = d // 131

answer = v[min(v.keys())]

class Problem357(unittest.TestCase):
    def test(self):
        assert str(answer) == get_correct_answer(14, 357)

if __name__ == '__main__':
    print(answer)