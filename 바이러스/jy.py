import sys
input = sys.stdin.readline

N = int(input())

M = int(input())

li = [[] for _ in range(N+1)]

for _ in range(M):
    
    fromV, toV = map(int, input().split())
    
    li[fromV].append(toV)
    li[toV].append(fromV)
    
def dfs(li, fromV):
    
    visit = []
    stack = []
    
    stack.append(fromV)
    
    while stack:
        
        node = stack.pop()
        
        if node not in visit:
            visit.append(node)
            stack.extend(li[node])
            
    return visit

print(len(dfs(li, 1))-1)
