import sys
from collections import defaultdict, deque

'''
입력
'''
n = int(sys.stdin.readline())
node = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]


'''
각 노드들을 연결
'''
graph = defaultdict(list)
for e, v in node:
    graph[e].append(v)
    graph[v].append(e)

'''
bfs 준비
visit -> 1번부터 n 번까지
root -> 1로 고정 (문제조건)
q -> 1부터 시작
child_parent -> bfs로 순회하면서 자식 - 부모를 저장하는 dict
'''
visit = [False] * (n + 1)
root = 1
q = deque([root])
child_parent = defaultdict(int)


'''
bfs 시작
'''
while q:
    parent = q.popleft()
    child_node = graph[parent]

    for child in child_node:
        if not visit[child]:  # 방문하지 않았으면
            visit[child] = True  # 방문 표시
            child_parent[child] = parent  # 해당 자식과 부모 노드 기록
            q.append(child)  # q에 넣어줌

'''
2번부터 n번 노드의 부모노드 출력
'''
for child in range(2, n + 1):
    print(child_parent[child])
