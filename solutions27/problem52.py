from random import randint


def bruteforce(a):
    answer = 0
    for i1 in range(len(a)):
        for i2 in range(i1 + 1, len(a)):
            for i3 in range(i2 + 1, len(a)):
                s = a[i1] + a[i2] + a[i3]
                if s > answer and s % 3 == 0:
                    answer = s
    return answer


def efficient(a):
    m = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    for x in a:
        m[x % 3].append(x)
        m[x % 3].sort(reverse = True)
        m[x % 3] = m[x % 3][:3]

    return max([
        m[0][0] + m[1][0] + m[2][0], # выбираем максимальное число по каждому остатку 0, 1, 2.  Тогда сумма имеет остаток (0 + 1 + 2) % 3 = 0.
        sum(m[0]), # Выбираем три максимальных числа, делящихся на 3. Тогда сумма тоже делится на 3.
        sum(m[1]), # Выбираем три максимальных числа, дающих остаток 1 при делении на 3. Тогда сумма имеет остаток (1 + 1 + 1) % 3 = 0.
        sum(m[2]), # Выбираем три максимальных числа, дающих остаток 2 при делении на 3. Тогда сумма имеет остаток (2 + 2 + 2) % 3 = 0.
    ])

def test_bruteforce():
    test_cases = [
        ([1, 3, 6, 9], 9 + 6 + 3),
        ([5, 5, 4, 13, 7, 10], 30),
    ]
    for test_case in test_cases:
        data, answer = test_case
        actual = bruteforce(data)
        assert actual == answer, f'Не пройден тест {data}: ожидалось {answer}, получено {actual}'
    print('Bruteforce тесты пройдены')


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

with open('./data/27data/52/27-52a.txt') as f:
    for line in f.readlines():
        dataA.append(int(line))

with open('./data/27data/52/27-52b.txt') as f:
    for line in f.readlines():
        dataB.append(int(line))

print(f'Длина массива A:', len(dataA))
print(f'Длина массива B:', len(dataB))

test_bruteforce()
print(f'bruteforce, список A:', bruteforce(dataA))

random_tests(test_count=1000)

print(f'efficient, список A:', efficient(dataA))
print(f'efficient, список B:', efficient(dataB))
