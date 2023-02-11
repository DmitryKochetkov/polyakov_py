import unittest
from answers import get_correct_answer

def prev(x):
    s = str(x)
    s2 = ''
    for c in s:
        if c == '0':
            return []
        s2 += str(int(c) - 1)
    
    result = [int(s2)]
    if s[-1] == '9':
        result.append(result[0] + 1)
    return result

def solve():
    dp = [0] * 52
    dp[25] = 1
    for i in range(26, 52):
        dp[i] = dp[i-1]
        for item in prev(i):
            dp[i] += dp[item]

    return dp[51]

class Problem21(unittest.TestCase):
    def test(self):
        actual = solve()
        expected = get_correct_answer(23, 21)
        assert actual == expected, f'Expected {expected}, actual {actual}'

if __name__ == '__main__':
    print(solve())