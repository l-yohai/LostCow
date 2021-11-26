import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]
nums.extend(list(map(int, input().split())))

dp = [0] * (n + 1)
dp[1] = nums[1]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + nums[i]
for _ in range(m):
    i, j = map(int, input().split())

    print(dp[j] - dp[i - 1])
