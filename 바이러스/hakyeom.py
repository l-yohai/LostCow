import sys
from collections import defaultdict, deque
input = sys.stdin.readline
num_of_computer = int(input())
num_of_network = int(input())

network = defaultdict(list)
for _ in range(num_of_network):
    node = list(map(int, input().split()))
    network[node[0]].append(node[1])
    network[node[1]].append(node[0])

q = deque([1])
visit = [False] * (num_of_computer + 1)
visit[1] = True
while q:
    cur_virus = q.popleft()
    for next_node in network[cur_virus]:
        if not visit[next_node]:
            visit[next_node] = True
            q.append(next_node)
            #cnt += 1

print(sum(visit) - 1)
