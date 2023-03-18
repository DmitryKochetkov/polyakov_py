dp = [0] * 36

dp[1] = 1
for i in range(2, 10+1):
    dp[i] = dp[i - 1]
    if i % 2 == 0:
        dp[i] += dp[i // 2]

for i in range(11, 36):
    if i == 17:
        dp[i] = 0
    else:
        dp[i] = dp[i-1]
        if i % 2 == 0 and i >= 20:
            dp[i] += dp[i // 2]
print(dp[35])