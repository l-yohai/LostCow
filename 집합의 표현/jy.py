import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(range(n + 1))


def find_root(tar):
    cur = arr[tar]
    path_list = [cur]
    while cur != arr[cur]:
        cur = arr[cur]
        path_list.append(cur)
    for node in path_list:
        arr[node] = cur
    return cur


def union(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a != root_b:
        if root_a > root_b:
            arr[root_a] = root_b
        else:
            arr[root_b] = root_a


for _ in range(m):
    t, a, b = map(int, input().split())

    if t == 0:
        union(a, b)
    else:
        if find_root(a) == find_root(b):
            print("YES")
        else:
            print("NO")
