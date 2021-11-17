import sys

input = sys.stdin.readline

n, m = map(int, input().split())

string_set = []
for _ in range(n):
    string_set.append(input().strip())
cnt = 0

subset_list = []
for _ in range(m):
    subset_string = input().strip()
    if not subset_string in subset_list:
        if subset_string in string_set:
            cnt += 1
            subset_list.append(subset_string)

print(cnt)
