from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

g = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

q = deque()
q.append((x, 0))
visit = [False] * (n + 1)
visit[x] = True
ans = []
while q:
    city, count = q.popleft()

    for next_city in g[city]:
        if visit[next_city] == False:
            if count + 1 == k:
                ans.append(next_city)
                continue
            else:
                q.append((next_city, count + 1))
                visit[next_city] = True
if not ans:
    print(-1)
else:
    print("\n".join(sorted(map(str, ans))))
