import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = defaultdict(list)
graph_cnt = dict()

for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

querys = [input().strip() for _ in range(q)]

visit = set()


def recur_count(node):
    global visit, graph_cnt

    visit.add(node)

    chs = []
    for next_node in graph[node]:
        if next_node not in visit:
            chs.append(next_node)
            recur_count(next_node)
    cnt = 0
    for ch in chs:
        cnt += graph_cnt[ch]
    graph_cnt[node] = cnt + 1


recur_count(r)

for query in map(int, querys):
    print(graph_cnt[query])
