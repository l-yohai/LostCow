import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]

directions = [(1,0), (0,1), (-1,0), (0, -1)]


ans = 0
while True:
    go_next = False
    total_visit = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in total_visit:
                po = populations[i][j]
                stack = []
                stack.append((i,j))
                visit = set()
                total_visit.add((i,j))
                visit.add((i,j))
                while stack:
                    x, y = stack.pop()
                    
                    for c, d in directions:
                        a = x+c
                        b = y+d
                        if 0<=a<N and 0<=b<N and (a,b) not in total_visit \
                            and L<=abs(populations[x][y]-populations[a][b])<=R:
                            total_visit.add((a,b))
                            visit.add((a,b))
                            stack.append((a,b))
                            po += populations[a][b]
                            go_next = True
                
                po = po//len(visit)
                for x, y in visit:
                    populations[x][y] = po
    if not go_next:
        break
    ans += 1
print(ans)

                
        
