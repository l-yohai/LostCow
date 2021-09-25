import sys

'''
인풋
'''
input = sys.stdin.readline
i, j = map(int, input().split())
district = [list(map(int, input().split())) for _ in range(i)]
k = int(input())
sub_district_point = [list(map(int, input().split())) for _ in range(k)]


'''
dp에 1,1 부터 각 row, col 까지의 사각형의 인구수를 더함
'''

dp = [[0] * (j + 1) for _ in range(i + 1)]

for y in range(i):
    for x in range(j):
        dp[y + 1][x + 1] = dp[y + 1][x] + \
            dp[y][x + 1] + district[y][x] - dp[y][x]

'''
dp에 저장된 값을 이용해
큰 직사각형에서 작은 직사각형을 빼고 겹치는 부분은 더해서 구함
'''

for point in sub_district_point:
    y1, x1, y2, x2 = point
    print(dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1])
