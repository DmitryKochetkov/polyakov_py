from random import randint
from itertools import product

def bruteforce(a):
    return 0

def efficient(a):
    return 0

def test_bruteforce():
    assert bruteforce([
        [1, 3, 2],
        [5, 12, 12],
        [6, 8, 12],
        [5, 4, 12],
        [3, 3, 12],
        [1, 1, 13],
    ]) == 63

def test_efficient(a):
    """
    Тестирует решения на заданном массиве.
    """
    expected = bruteforce(a)
    actual = efficient(a)
    assert expected == actual, f'Expected {expected}, actual {actual}'
    return actual

def random_tests(test_count=20):
    print(f'Запуск {test_count} случайных тестов...')
    for test_id in range(1, test_count+1):
        # генерирурем случайные данные
        n = 12
        a = [[randint(1, 100), randint(1, 100), randint(1, 100)] for i in range(n)]
        answer = test_efficient(a)
        print(f"Пройден тест #{test_id} на данных {a}. Ответ {answer}")

    print(f"Случайные тесты пройдены!")

dataA = []
dataB = []

with open('./data/27data/10/27-10a.txt') as f:
    for line in f.readlines():
        dataA.append(list(map(int, f.readline().split())))

with open('./data/27data/10/27-10b.txt') as f:
    for line in f.readlines():
        dataB.append(list(map(int, f.readline().split())))

print(f'Длина массива A:', len(dataA))
print(f'Длина массива B:', len(dataB))

test_bruteforce()
print(f'bruteforce, список A:', bruteforce(dataA))

random_tests(test_count=1000)

print(f'efficient, список A:', efficient(dataA))
print(f'efficient, список B:', efficient(dataB))


