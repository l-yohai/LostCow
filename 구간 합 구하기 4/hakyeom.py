import sys

input = sys.stdin.readline
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(len(dp) - 1):
    dp[i + 1] += dp[i] + numbers[i]

for i in range(m):
    i, j = map(int, input().split())

    print(dp[j] - dp[i - 1])

# 구간합 -> 리스트 i번째에 i부터 0까지의 합을 저장해둠
