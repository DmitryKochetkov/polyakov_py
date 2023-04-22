from random import randint

def bruteforce(a):
    n = len(a)
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            x = a[i] * a[j]
            if x % 7 == 0 and x % 49 != 0 and x > result:
                result = x

    return result

def efficient(a):
    m7 = 0
    m = 0
    n = len(a)

    for x in a:
        if x % 7 == 0 and x % 49 != 0 and x > m7:
            m7 = x
        elif x % 7 != 0 and x > m:
            m = x

    return m7 * m
    
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
        a = [randint(1, 100) for i in range(n)]
        answer = test_efficient(a)
        print(f"Пройден тест #{test_id} на данных {a}. Ответ {answer}")

    print(f"Случайные тесты пройдены!")

dataA = []
dataB = []

with open('./data/27data/7/27-7a.txt') as f:
    for line in f.readlines():
        dataA.append(int(line))

with open('./data/27data/7/27-7b.txt') as f:
    for line in f.readlines():
        dataB.append(int(line))

print(f'Длина массива A:', len(dataA))
print(f'Длина массива B:', len(dataB))

# test_bruteforce()
print(f'bruteforce, список A:', bruteforce(dataA))

random_tests(test_count=1000)

print(f'efficient, список A:', efficient(dataA))
print(f'efficient, список B:', efficient(dataB))


