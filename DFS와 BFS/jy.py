from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

li = [[] for i in range(N + 1)]

for _ in range(M):
    fromV, toV = map(int, input().split())
    li[fromV].append(toV)
    li[toV].append(fromV)


def dfs(graph, fromV):

    for i in li:
        i.sort(reverse=True)

    visit = []
    stack = []

    stack.append(fromV)

    while stack:

        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


def bfs(graph, fromV):

    for i in li:
        i.sort()

    visit = []
    queue = deque()

    queue.append(fromV)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


print(*dfs(li, V))
print(*bfs(li, V))
