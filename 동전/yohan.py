import sys
input = sys.stdin.readline

T = int(input())

while T:
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1

    for i in range(N):
        for j in range(coin[i], M + 1):
            dp[j] += dp[j - coin[i]]

    print(dp[M])
    T -= 1
