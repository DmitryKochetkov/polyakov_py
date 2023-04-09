# 75 задача из файла 27 с сайта Полякова

def bruteforce(a):
    """
    Неэффективное решение за O(n^3) (два вложенных for по n итераций, в каждом из которых считается сумма на подотрезке - еще порядка n итераций).
    Аргумент a - список чисел.
    Вместо самого ответа в целях дебага возвращается кортеж с границами результирующего подотрезка.
    """
    n = len(a)
    m = 0
    answer = n
    result_subsegment = None
    for l in range(n):
        for r in range(l+1, n):
            s = sum(a[l:(r+1)])
            if s % 43 == 0:
                if s > m:
                    m = s
                    result_subsegment = (l, r)
                    answer = r-l+1
                elif s == m:
                    result_subsegment = (l, r)
                    answer = min(answer, r-l+1)
    return answer, result_subsegment


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
    for i in range(1, n):
        q = p[i] % k
        if first[q] == -1:
            first[q] = i
    m = 0
    answer = n
    result_subsegment = (None, None)

    # перебираем ТОЛЬКО правую границу подотрезка
    for r in range(n-1):
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
                # result_subsegment = (None, None)
            elif s == m and length < answer:
                result_subsegment = (l, r)
                answer = length
    
    return answer, result_subsegment


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

print('Bruteforce решение пункта A: ', bruteforce(dataA))
print('Эффективное решение пункта A: ', efficient(dataA))
print(sum(dataA[587:776]), sum(dataA[587:776]) % 43)
print(sum(dataA[401:586]), sum(dataA[401:586]) % 43)
print('Эффективное решение пункта B: ', efficient(dataB))