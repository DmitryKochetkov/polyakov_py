dp = [0] * 16
dp[2] = 1
for i in range(3, 15+1):
    dp[i] = dp[i-1]
    if i % 2 == 0 and i // 2 >= 2:
        dp[i] += dp[i // 2]
dp[15]