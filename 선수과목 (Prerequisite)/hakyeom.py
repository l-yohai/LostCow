import sys
from collections import defaultdict, deque

# 실패코드
input = sys.stdin.readline
n, m = map(int, input().split())
prerequisite = defaultdict(list)
temp = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    prerequisite[a].append(b)
    temp[b].append(a)

ans = [[]] * (n + 1)

for i in range(1, n + 1):
    ans[i] = temp[i]


root_nodes = []

for i in range(1, len(ans)):
    if not ans[i]:
        root_nodes.append(i)

# print(root_nodes)
q = deque()
depth = 0
for node in root_nodes:
    q.append([depth, prerequisite[node]])

cnt_dict = defaultdict(int)

while q:
    cur_depth, next_nodes = q.popleft()

    for next_node in next_nodes:
        cnt_dict[next_node] = max(cnt_dict[next_node], cur_depth + 1)
        q.append([cur_depth + 1, prerequisite[next_node]])


# print(cnt_dict)
ans = []
for i in range(1, n + 1):
    ans.append(str(cnt_dict[i] + 1))

print(" ".join(ans))

# 성공코드 https://cseella.tistory.com/128
# 위상정렬이 뭔데 씹덕아!
