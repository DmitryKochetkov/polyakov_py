from random import randint

def bruteforce(a):
    """
    Неэффективное решение за O(n^3) (два вложенных for по n итераций, в каждом из которых считается сумма на подотрезке - еще порядка n итераций).
    Аргумент a - список чисел.
    Вместо самого ответа в целях дебага возвращается кортеж с границами результирующего подотрезка.
    """
    n = len(a)
    m = 0
    result_length = n
    result_subsegment = None
    k = 43
    for l in range(n):
        for r in range(l+1, n):
            s = sum(a[l:r+1])
            if s % k == 0:
                if s > m:
                    m = s
                    result_subsegment = (l, r)
                    result_length = r-l+1
                elif s == m and r-l+1 < result_length:
                    result_length = r-l+1
                    result_subsegment = (l, r)

    if result_subsegment != None:
        l, r = result_subsegment
        assert sum(a[l:(r+1)]) % k == 0, f'не пройдена финальная проверка ответа {result_subsegment}: s % {k} = {sum(a[l:r+1]) % k == 0}'
    return result_subsegment


def efficient(a):
    """
    Эффективное решение за O(n).
    Аргумент a - список чисел.

    Везде где написано "подотрезок", имеется ввиду непрерывная подпоследовательность.
    
    Вместо самого ответа в целях дебага возвращается кортеж с границами результирующего подотрезка.
    """
    # Сначала составим массив префикс-сумм p
    n = len(a)
    p = [0] * n 
    p[0] = a[0]
    for i in range(1, n):
        p[i] = p[i-1] + a[i]
    p = [0] + p # для устранения проблем с l = 0

    # сумма на подотрезке от l до r теперь вычисляется за O(1) как p[r+1] - p[l]
    # p[i+1] = сумма элементов с индексами от 0 до i включительно

    # Ускорения до O(n^2) все еще недостаточно, так как в файле B более миллиона чисел. Нужно ускорить до O(n).

    k = 43
    first = [-1] * k # first[i] - наимешьний индекс элемента из p, такой что a[first[i]] % k == i.
    # for i in range(1, n):
    for i in range(n):
        q = p[i] % k
        if first[q] == -1:
            first[q] = i
    m = 0
    answer = n
    result_subsegment = None

    # перебираем ТОЛЬКО правую границу подотрезка
    for r in range(n):
        # Вычислим левую границу. 
        # Для того, чтобы сумма a[l:(r+1)] была кратна k, нужно взять в качестве левого индекса такой l, что p[l] % k == p[r] % k.
        # При этом для максимизации суммы нужно брать первый такой индекс.
        q = p[r+1] % k
        l = first[q]

        if l != -1 and l < r:
            length = r-l+1
            s = p[r+1] - p[l] # теперь s - максимальная сумма среди всех подотрезков с правой границей r
            assert s % k == 0, f'Некорректное вычисление s на подотрезке ({l}, {r}): сумма s равна {s}, s % {k} = {s % k}. p[r+1] % k: {p[r+1] % k}. p[l] % k: {p[l] % k}'
            if s > m:
                m = s
                result_subsegment = (l, r)
                answer = length
            elif s == m and length < answer:
                result_subsegment = (l, r)
                answer = length
    
    if result_subsegment != None:
        l, r = result_subsegment
        assert sum(a[l:(r+1)]) % k == 0, f'не пройдена финальная проверка ответа {result_subsegment}: s % k = {sum(a[l:(r+1)]) % k == 0}'
    return result_subsegment

def test(a):
    """
    Тестирует решения на заданном массиве.
    """
    expected = bruteforce(a)
    actual = efficient(a)
    if expected == None and actual == None:
        return
    assert expected != None and actual != None, f'Не пройден тест на данных {a}. Bruteforce: {expected}, efficient {actual}.'

    l_expected = expected[1] - expected[0]
    l_actual = actual[1] - actual[0]
    s_expected = sum(a[expected[0]:expected[1]+1])
    s_actual = sum(a[actual[0]:actual[1]+1])
    assert l_expected == l_actual, f'Не пройден тест на данных {a}. Bruteforce: {expected} - сумма {s_expected}, efficient {actual} - сумма {s_actual}.'

def random_tests(test_count = 20):
    print(f'Запуск {test_count} случайных тестов...')
    for test_id in range(1, test_count+1):
        # генерирурем случайные данные
        n = 12
        a = [randint(1, 100) for i in range(n)]
        test(a)
        print(f"Пройден тест #{test_id} на данных {a}")
    
    print(f"Случайные тесты пройдены!")

dataA = []
dataB = []
with open('./data/27data/75/27-75a.txt') as f:
    n = f.readline()
    for line in f.readlines():
        dataA.append(int(line))

with open('./data/27data/75/27-75b.txt') as f:
    n = f.readline()
    for line in f.readlines():
        dataB.append(int(line))

random_tests()
l, r = bruteforce(dataA)
print(f'Переборное решение пункта A: отрезок {(l, r)}, длина {r-l+1}, сумма {sum(dataA[l:r+1])}')
l, r = efficient(dataA)
print(f'Эффективное решение пункта A: отрезок {(l, r)}, длина {r-l+1}, сумма {sum(dataA[l:r+1])}')

print(sum(dataA[587:776]), sum(dataA[587:776]) % 43)
print(sum(dataA[401:586]), sum(dataA[401:586]) % 43)
l, r = efficient(dataB)
print(f'Эффективное решение пункта B: отрезок {(l, r)}, длина {r-l+1}, сумма {sum(dataB[l:r+1])}')

