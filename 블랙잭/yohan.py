import sys


input = sys.stdin.readline

N, M = list(map(int, input().split()))

nums = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tmp = nums[i] + nums[j] + nums[k]
            if tmp > answer and tmp <= M:
                answer = tmp

print(answer)
