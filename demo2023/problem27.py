from math import ceil
# from ..utils import *
# from ..utils.data import *

capacity = 36

def bruteforce(a):
    n = len(a)
    min_cost = 10 ** 10
    optimal_start = 1

    for i in range(n): # проходимся по способам выбрать пункт для лаборатории
        start = a[i][0]
        cost = 0

        for j in range(n):
            if j != i:
                x, p = a[j]
                cost += abs(x - start) * p
        
        if cost < min_cost:
            min_cost = cost
            optimal_start = start

    return min_cost

def efficient(a):
    n = len(a)
    # Считаем стоимость при условии, что лаборатория установлена в первом пункте
    cost = 0
    start = a[0][0]
    ps = [0] * n # префикс-сумма по p
    ps[0] = a[0][1]
    # Считаем начальную стоимость
    for i in range(n):
        x, p = a[i]
        cost += abs(x - start) * p

    for i in range(1, n):
        ps[i] = ps[i-1] + a[i][1]

    min_cost = cost
    optimal_start = 0

    for i in range(1, n):
        cost = cost + (a[i][0] - a[i-1][0]) * (ps[i-1] - ps[n-1] + ps[i-1])
        # print(cost)
        if cost < min_cost:
            min_cost = cost
            optimal_start = i

    return min_cost



with open('./27_B.txt') as f:
    n = int(f.readline())
    a = list()
    for line in f.readlines():
        x, p = map(int, line.split())
        a.append((x, ceil(p / capacity))) # Заменяем p на p со звездочкой
    
    # print('REAL', bruteforce(a))
    print(efficient(a))