import sys

input = sys.stdin.readline

poly1 = "AAAA"
poly2 = "BB"

boards = input().strip()

board_split = boards.split(".")

divied_by_ploy2 = []
is_passible = True
for board in board_split:
    if board != "":
        if len(board) % 2 == 0:
            divied_by_ploy2.append(len(board) // 2)
        else:
            is_passible = False
    if not is_passible:
        break

if is_passible:
    ans = []
    for max_poly in divied_by_ploy2:
        temp = []
        temp.append(max_poly // 2)
        temp.append(max_poly % 2)
        ans.append(temp)

    ans = list(map(lambda x: "AAAA" * x[0] + "BB" * x[1], ans))

    ans_text = ""
    idx = 0
    ans_idx = 0
    while ans_idx < len(ans):
        if boards[idx] == ".":
            ans_text += "."
            idx += 1
        else:
            ans_text += ans[ans_idx]
            idx += len(ans[ans_idx])
            ans_idx += 1
    ans_text += boards[idx:]
    print(ans_text)
else:
    print(-1)
