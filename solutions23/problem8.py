import unittest
from answers import get_correct_answer

def solve1():
    dp = [0] * 16
    dp[1] = 1
    for i in range(2, 16):
        dp[i] = dp[i-1]
        if i >= 3:
            dp[i] += dp[i-3]
        if i % 3 == 0:
            dp[i] += dp[i // 3]

    return dp[15]

def solve2(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return solve2(start + 1, end) + solve2(start + 3, end) + solve2(start * 3, end)

class Problem8(unittest.TestCase):
    def test(self):
        actual = solve1()
        expected = get_correct_answer(23, 8)
        assert actual == expected, f'Expected {expected}, actual {actual}'

        actual = solve2(1, 15)
        expected = get_correct_answer(23, 8)
        assert actual == expected, f'Expected {expected}, actual {actual}'

if __name__ == '__main__':
    print(solve1())