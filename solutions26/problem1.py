import unittest
from answers import get_correct_answer

with open('./data/26data/26-1.txt') as f:
    s, n = map(int, f.readline().split())
    a = list(map(int, f.readlines()))
    used_space = 0

    a.sort()

    n_saved = 0
    last_user = None
    max_file = 0

    for i in range(n):
        if used_space + a[i] <= s:
            used_space += a[i]
            n_saved += 1
            last_user = i
            max_file = max(a[i], max_file)
        else:
            break
    
    # Сейчас сохранены файлы n_saved пользователей
    for user in range(last_user+1, n):
        if used_space - a[last_user] + a[user] <= s and a[user] > max_file:
            used_space = used_space - a[last_user] + a[user]
            max_file = max(a[user], max_file)
            last_user = user
            # n_saved не меняется, так как мы убрали один файл, и сохранили вместо него другой

class Problem1(unittest.TestCase):
    def test(self):
        actual = [n_saved, max_file]
        expected = list(map(int, get_correct_answer(26, 1).split()))
        assert actual == expected, f'Actual: {actual}, expected: {expected}'

if __name__ == '__main__':
    print(i, used_space)

