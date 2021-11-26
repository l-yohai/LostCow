import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

v = 0
prefix_sum = [0]

for num in nums:
    v += num
    prefix_sum.append(v)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
