"""import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    coins = list(map(int, input().split()))
    money = int(input())

    dp = [[0] * len(coins) for _ in range(money + 1)]
    dp[0] = [1] + [0] * (len(coins) - 1)
    for m in range(money + 1):
        for coin_idx in range(len(coins)):
            if m - coins[coin_idx] >= 0:
                for coin_idx2 in range(coin_idx + 1):
                    dp[m][coin_idx] += dp[m - coins[coin_idx]][coin_idx2]
    print(sum(dp[money]))


"""
