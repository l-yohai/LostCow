import sys

input = sys.stdin.readline

s = int(input())

num = 1
sum = 0
cnt = 0
while sum <= s:
    sum += num
    num += 1
    cnt += 1
print(cnt - 1)
