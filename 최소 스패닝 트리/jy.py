import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

arr = list(range(v + 1))

ans = 0


def find_root(node):
    cur = arr[node]
    path_list = [cur]

    while cur != arr[cur]:
        cur = arr[cur]
        path_list.append(cur)

    for tnode in path_list:
        arr[tnode] = cur

    return cur


for a, b, c in graph:
    root_a = find_root(a)
    root_b = find_root(b)

    if root_a != root_b:
        ans += c
        if root_a < root_b:
            arr[root_a] = root_b
        else:
            arr[root_b] = root_a

print(ans)
