import sys

input = sys.stdin.readline

n, m = map(int, input().split())

string_set = {}
for _ in range(n):
    string_set[input().strip()]  = 0
cnt = 0

for _ in range(m):
    subset_string = input().strip()
    if subset_string in string_set:
        cnt += 1

print(cnt)
