from collections import defaultdict, deque


N = int(input())

tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
visit = [False]*(N+1)
q.append(1)

visit[1] = True
parent_arr = [-1]*(N+1)

while q:
    node = q.popleft()
    for next_node in tree[node]:
        if visit[next_node]==False:
            visit[next_node] = True
            parent_arr[next_node] = node
            q.append(next_node)
print('\n'.join(map(str, parent_arr[2:])))
