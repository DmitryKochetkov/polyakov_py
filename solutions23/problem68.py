import unittest
from answers import get_correct_answer

def solve():
    """
    Исполнитель Июнь15 преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:

    1. Прибавить 1
    2. Умножить на 2

    Первая команда увеличивает число на экране на 1, вторая умножает его на 2. Программа для исполнителя Июнь15 – это последовательность команд.
    Сколько существует программ, для которых при исходном числе 2 результатом является число 31 и при этом траектория вычислений 
    содержит число 15 и не содержит число 22?

    """
    dp = [0] * 16
    dp[2] = 1
    for i in range(3, 15+1):
        dp[i] = dp[i-1]
        if i % 2 == 0 and i // 2 >= 2:
            dp[i] += dp[i // 2]

    dp2 = [0] * 32
    dp2[15] = 13
    for i in range(16, 31+1):
        if i == 22:
            dp2[i] = 0
        else:
            dp2[i] = dp2[i-1]
            if i % 2 == 0 and i // 2 >= 15:
                dp2[i] += dp2[i // 2]
    
    return dp2[31]

class Problem68(unittest.TestCase):
    def test(self):
        assert int(solve()) == int(get_correct_answer(23, 68))

if __name__ == '__main__':
    print(solve())