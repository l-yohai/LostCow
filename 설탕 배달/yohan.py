n = int(input())

dp = [5001] * 5001
dp[3] = 1
dp[5] = 1

for i in range(5, n + 1):
    dp[i] = min(dp[i], dp[i - 3] + 1, dp[i - 5] + 1)

if dp[n] == 5001:
    dp[n] = -1
print(dp[n])
