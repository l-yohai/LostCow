import sys

n, m = map(int, input().split())

s = []
for _ in range(n):
    s.append(sys.stdin.readline())

check_str = []
for _ in range(m):
    check_str.append(sys.stdin.readline())

count = 0
for i in range(m):
    if check_str[i] in s:
        count += 1
print(count)
