import sys
from collections import deque

n, m, k, x = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False for _ in range(n + 1)]

answer = []
q = deque()
q.append((x, 0))

while q:
    city, count = q.popleft()
    if count == k:
        answer.append(city)
    elif count < k:
        for i in graph[city]:
            if not visited[i]:
                visited[i] = True
                q.append((i, count + 1))

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)
