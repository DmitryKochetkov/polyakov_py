from random import randint

def positive_numbers(path):
    """
    Генерирует входные данные в виде набора натуральных чисел, каждое из которых записано на новой строке.
    """
    with open(path, 'w+') as f:
        n = 15
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 10000)) + '\n')

def positive_pairs(path):
    """
    Генерирует входные данные в виде набора пар натуральных чисел.
    """
    with open(path, 'w+') as f:
        n = 10
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 100000)) + ' ' + str(randint(1, 100000)) + '\n')

def positive_triplets(path):
    """
    Генерирует входные данные в виде набора троек натуральных чисел.
    """
    with open(path, 'w+') as f:
        n = 10
        f.write(str(n) + '\n')

        for i in range(n):
            f.write(str(randint(1, 100000)) + ' ' + str(randint(1, 100000)) + ' ' + str(randint(1, 100000)) + '\n')
