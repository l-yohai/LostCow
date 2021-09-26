import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
li = [None]
for i in range(1, N+1):
    po = input().strip()
    dic[po] = i
    li.append(po)

for _ in range(M):
    x = input().strip()
    try:
        x = int(x)
        print(li[x])
    except:
        print(dic[x])
