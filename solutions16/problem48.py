import unittest
from answers import get_correct_answer
from tqdm import tqdm

def F(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return n + F(n-1)
    else:
        return n*n + F(n-2)

dp = [0] * (10 ** 8)
for i in tqdm(range(1, int(1e8))):
    if i <= 3:
        dp[i] = i
    elif i % 2 == 0:
        dp[i] = i + dp[i-1]
    else:
        dp[i] = i*i + dp[i-2]

def solve():
    c = 0
    for i in tqdm(range(1, int(1e8))):
        if dp[i] <= 10 ** 8:
            c += 1
    return c

class Problem48(unittest.TestCase):
    def test(self):
        for i in range(100):
            assert F(i) == dp[i]
        assert str(solve()) == get_correct_answer(16, 48)

if __name__ == '__main__':
    print(solve())