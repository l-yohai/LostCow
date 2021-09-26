import sys
from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
parents = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(current_node, parents):
    for i in graph[current_node]:
        if parents[i] == 0:
            parents[i] = current_node
            dfs(i, parents)


def bfs(current_node):
    q = deque()
    q.append(current_node)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if parents[i] == 0:
                parents[i] = node
                q.append(i)


dfs(1, parents)
# bfs(1)

for i in range(2, n + 1):
    print(parents[i])
