import unittest
from answers import get_correct_answer

def solve():
    dp = [0] * 16
    dp[1] = 1
    for i in range(2, 16):
        dp[i] = dp[i-1]
        if i % 2 == 0:
            dp[i] += dp[i // 2]
        else:
            dp[i] += dp[(i - 1) // 2]
        
        if i % 10 == 0:
            dp[i] += dp[i // 10]

    return dp[15]

class Problem35(unittest.TestCase):
    def test(self):
        actual = solve()
        expected = get_correct_answer(23, 35)
        assert actual == expected, f'Expected {expected}, actual {actual}'

if __name__ == '__main__':
    print(solve())