# https://www.acmicpc.net/problem/14929
import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))


"""
x0 (x1 + x2 + ... xn)
x1 (x2 + x3 + ... xn)
.
.
.
xn-1 (xn)
"""

xb_max = sum(x[1:])
dp = [xb_max]
for b in range(1, len(x) - 1):
    dp.append(dp[-1] - x[b])

sigma = 0
for a in range(0, len(x) - 1):
    sigma += x[a] * dp[a]


print(sigma)
