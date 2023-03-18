import unittest
from answers import get_correct_answer

def solve():
    dp = [0] * 23
    dp[22] = 1
    for i in range(21, 1, -1):
        dp[i] = dp[i+1]
        if i + 3 <= 22:
            dp[i] += dp[i+3]
        
        if i < 4:
            p = 1
            while p * 4 + i <= 22:
                dp[i] += dp[p * 4 + i]
                p += 1

    return dp[2]

class Problem94(unittest.TestCase):
    def test(self):
        actual = solve()
        expected = get_correct_answer(23, 94)
        assert actual == expected, f'Expected {expected}, actual {actual}'

if __name__ == '__main__':
    print(solve())