import sys

n = int(input())

m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white_count, blue_count = 0, 0


def split_paper(x, y, n):
    global white_count, blue_count

    is_same_color = m[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if is_same_color != m[i][j]:
                split_paper(x, y, n // 2)
                split_paper(x + n // 2, y, n // 2)
                split_paper(x, y + n // 2, n // 2)
                split_paper(x + n // 2, y + n // 2, n // 2)
                return

    if is_same_color == 0:
        white_count += 1
    else:
        blue_count += 1
    return


split_paper(0, 0, n)
print(white_count)
print(blue_count)
