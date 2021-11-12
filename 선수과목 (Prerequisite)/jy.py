import sys
from collections import deque, defaultdict


input = sys.stdin.readline

n, m = map(int, input().split())

indegrees = [0] * (n + 1)
outdegrees = [0] * (n + 1)

answers = [0] * (n + 1)

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1
    outdegrees[a] += 1

start_list = []
for idx in range(1, n + 1):
    if indegrees[idx] == 0:
        start_list.append((idx, 1))
        answers[idx] = 1

q = deque(start_list)

while q:
    node, cnt = q.popleft()
    for next_node in graph[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node] == 0:
            q.append((next_node, cnt + 1))
            answers[next_node] = cnt + 1

print(" ".join(map(str, answers[1:])))
