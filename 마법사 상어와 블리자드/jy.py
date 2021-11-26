import sys
from copy import copy

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
blizards = [list(map(int, input().split())) for _ in range(m)]


def board_to_list(board):
    ret_li = []
    ret_li.extend(board[0])

    r, c = 0, n - 1
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    d_idx = 0

    for k in range(n - 1, 1, -1):
        for _ in range(1, k + 1):
            r, c = r + d[d_idx][0], c + d[d_idx][1]
            ret_li.append(board[r][c])
        d_idx += 1
        d_idx %= 4
        for _ in range(1, k + 1):
            r, c = r + d[d_idx][0], c + d[d_idx][1]
            ret_li.append(board[r][c])
        d_idx += 1
        d_idx %= 4

    ret_li.append(board[r + d[d_idx][0]][c + d[d_idx][1]])
    ret_li.append(0)

    return list(reversed(ret_li))


def list_to_board(board_list):
    board = [[0] * (n) for _ in range(n)]
    board_list.reverse()
    board[0] = board_list[:n]

    idx = n
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    d_idx = 0

    r, c = 0, n - 1

    for k in range(n - 1, 1, -1):
        for _ in range(1, k + 1):
            r, c = r + d[d_idx][0], c + d[d_idx][1]
            board[r][c] = board_list[idx]
            idx += 1
        d_idx += 1
        d_idx %= 4
        for _ in range(1, k + 1):
            r, c = r + d[d_idx][0], c + d[d_idx][1]
            board[r][c] = board_list[idx]
            idx += 1
        d_idx += 1
        d_idx %= 4

    board[r + d[d_idx][0]][c + d[d_idx][1]] = board_list[idx]

    return board


def push_and_remove_zero(board):
    board_list = board_to_list(board)
    board_str = "".join(map(str, board_list))
    board_str = board_str.replace("0", "")
    board_list = list(map(int, list(board_str)))
    board_list += [0] * (n * n - len(board_list) - 1)
    board_list = [0] + board_list

    board = list_to_board(board_list)

    return board


def blizard_on_board(board, d, s):
    board = copy(board)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dr, dc = directions[d - 1]

    for i in range(1, s + 1):
        board[n // 2 + dr * i][n // 2 + dc * i] = 0

    return push_and_remove_zero(board)


def explosion(board):
    board_list = board_to_list(board)
    idx = n ** 2 - 1
    cnt = 0
    pre_num = -1

    result = [0, 0, 0]

    while idx >= 1:
        if board_list[idx] == 0:
            pre_num = board_list[idx]
            cnt = 1
        elif board_list[idx] == pre_num:
            cnt += 1
        else:
            if cnt >= 4:
                result[pre_num - 1] += cnt
                board_list = board_list[: idx + 1] + board_list[idx + 1 + cnt :]
            cnt = 1
            pre_num = board_list[idx]
        idx -= 1
    if cnt >= 4:
        result[pre_num - 1] += cnt
        board_list = board_list[: idx + 1] + board_list[idx + 1 + cnt :]

    board_list += [0] * (n * n - len(board_list))

    return push_and_remove_zero(list_to_board(board_list)), result


def modify(board):
    board_list = board_to_list(board)
    idx = 1
    cnt = 0
    pre_num = -1
    modified_list = []

    while idx < n * n and len(modified_list) <= n * n:
        if board_list[idx] == 0:
            if pre_num != -1:
                modified_list.extend([cnt, pre_num])
            break
        elif board_list[idx] == pre_num:
            cnt += 1
        else:
            if pre_num != -1:
                modified_list.extend([cnt, pre_num])
            cnt = 1
            pre_num = board_list[idx]
        idx += 1

    modified_list = [0] + modified_list[: n * n - 1]
    modified_list += [0] * (n * n - len(modified_list))
    return list_to_board(modified_list)


ans = [0, 0, 0]
for d, s in blizards:
    board = blizard_on_board(board, d, s)
    result = [-1, -1, -1]
    while result != [0, 0, 0]:
        board, result = explosion(board)
        ans[0] += result[0]
        ans[1] += result[1]
        ans[2] += result[2]
    board = modify(board)

print(ans[0] + 2 * ans[1] + 3 * ans[2])
