import sys

input = sys.stdin.readline
# asdfasdf
test_case = int(input().strip())
for i in range(test_case):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    total = int(input().strip())

    dp = [0] * (total + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], total + 1):
            dp[j] += dp[j - coins[i]]

    print(dp[total])
