from collections import deque

N, K = map(int, input().split())

q = deque(range(1, N+1))
ans = []

for _ in range(N):
    q.rotate(-K+1)
    ans.append(q.popleft())

print('<'+ ', '.join(map(str, ans))+'>')