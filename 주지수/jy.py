import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
nums = [list(map(int, input().split())) for _ in range(K)]
nums = [(x1-1, y1-1, x2-1, y2-1) for x1, y1, x2, y2 in nums]

dp = [[0]*M for _ in range(N)]
row_dp = [[0]*M for _ in range(N)]
col_dp = [[0]*M for _ in range(N)]

dp[0][0] = arr[0][0]
row_dp[0][0] = arr[0][0]
col_dp[0][0] = arr[0][0]

for i in range(1, N):
    row_dp[i][0] = arr[i][0]
    dp[i][0] = dp[i-1][0] + arr[i][0]
for i in range(N):
    for j in range(1, M):
        row_dp[i][j] = row_dp[i][j-1] + arr[i][j]
for j in range(1, M):
    col_dp[0][j] = arr[0][j]
    dp[0][j] = dp[0][j-1] + arr[0][j]
for i in range(1, N):
    for j in range(M):
        col_dp[i][j] = col_dp[i-1][j] + arr[i][j]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j-1] + col_dp[i][j] + row_dp[i][j] - arr[i][j]

def get_sum(x1, y1, x2, y2):
    if x1>x2 or y1>y2:
        return 0
    elif x1==0 and y1==0:
        return dp[x2][y2]
    else:
        return get_sum(0, 0, x2, y2) - get_sum(0, 0, x2, y1-1) \
            - get_sum(0, 0, x1-1, y2) + get_sum(0,0, x1-1, y1-1)

for x1, y1, x2, y2 in nums:
    print(get_sum(x1, y1, x2, y2))

