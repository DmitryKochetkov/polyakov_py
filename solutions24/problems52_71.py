import unittest
from answers import get_correct_answer
from .utils import get_file_path

def solve(s):
    answer = 0
    character = s[0]
    a = 1

    for i in range(1, len(s)):    
        if s[i] == s[i-1]:
            a += 1
            if a > answer:
                character = s[i]
                answer = a
        else:
            a = 1

    return '{} {}'.format(character, answer)

class Problems52_71(unittest.TestCase):
    def test(self):
        for i in range(52, 69):
            if i != 68: # Для 68 задачи ответ в таблице некорректен (issue #7)
                with open(get_file_path(i)) as f:
                    assert solve(f.read()) == get_correct_answer(24, i), 'Expected {}, actual {}'.format(get_correct_answer(24, i), solve(f.read()))

if __name__ == '__main__':
    print('Not implemented yet.')