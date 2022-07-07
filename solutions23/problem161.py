from itertools import *
import unittest
from answers import get_correct_answer

def solve():
    """
    (Б. Михлин) Исполнитель К22 преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера: 

    1. Прибавь 1
    2. Прибавь 3
    3. Получи число Фибоначчи по номеру

    Первая из них увеличивает число на экране на 1, вторая увеличивает число на 3. Третья команда получает число из ряда Фибоначчи
    c номером, равным числу на экране (например, для числа 6 будет получено 8, а для числа 7 будет получено 13). 
     
    Программа для исполнителя – это последовательность команд.
    Сколько существует программ, которые преобразуют исходное число 6 в число 21?
    """
    p = [0]*22
    p[6] = 1
    for i in range(7,22):
        p[i] += p[i-1] + p[i-3]
        if i == 8:
            p[i] += p[6]
        if i == 13:
            p[i] += p[7]
        if i == 21:
            p[i] += p[8]
    
    return p[-1]

class Problem161(unittest.TestCase):
    def test(self):
        assert int(solve()) == int(get_correct_answer(23, 161))

if __name__ == '__main__':
    print(solve())