n, m = map(int, input().split())

table = []
for _ in range(n):
    table.append(input().split())

k = int(input())
squares = []
for _ in range(k):
    squares.append(input().split())

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] += int(table[i - 1][j - 1]) + dp[i - 1][j] + \
            dp[i][j - 1] - dp[i - 1][j - 1]

for i in range(len(squares)):
    x1, y1, x2, y2 = map(int, squares[i])
    answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(answer)
