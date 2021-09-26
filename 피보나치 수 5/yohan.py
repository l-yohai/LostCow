def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return dp[n]


n = int(input())

dp = [0] * 21
dp[0] = 0
dp[1] = 1
print(fibonacci(n))
