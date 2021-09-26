# https://www.acmicpc.net/problem/1620

import sys

n, m = list(map(int, sys.stdin.readline().split()))

N = list(sys.stdin.readline().strip() for _ in range(n))
M = list(sys.stdin.readline().strip() for _ in range(m))

name_idx = {}

for i in range(n):
    name, idx = N[i], i + 1
    name_idx[name] = idx

idx_name = {v: k for k, v in name_idx.items()}


for question in M:
    if question.isdigit():
        print(idx_name[int(question)])
    else:
        print(name_idx[question])
