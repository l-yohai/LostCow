import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    node1, node2 = map(int, input().split())
    if not node2 in graph[node1]:
        graph[node1].append(node2)
    if not node1 in graph[node2]:
        graph[node2].append(node1)

for i in range(1, n + 1):
    graph[i] = sorted(list(set(graph[i])))

dfs_path = []
dfs_visit = [False] * (n + 1)


def dfs(node):
    if not dfs_visit[node]:  # 방문하지 않았으면
        dfs_visit[node] = True  # 방문표시
        dfs_path.append(node)  # path 기록
        for next_node in graph[node]:
            dfs(next_node)


dfs_path.append(v)
dfs_visit[v] = True
for node in graph[v]:
    dfs(node)

bfs_path = []
bfs_visit = [False] * (n + 1)

bfs_path.append(v)
bfs_visit[v] = True

q = deque([graph[v]])

while q:
    next_nodes = q.popleft()
    for next_node in next_nodes:
        if not bfs_visit[next_node]:
            bfs_visit[next_node] = True
            bfs_path.append(next_node)
            q.append(graph[next_node])

print(" ".join(str(x) for x in dfs_path))
print(" ".join(str(x) for x in bfs_path))
