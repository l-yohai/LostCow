board = input()

idx = 0
ans = ""

while idx < len(board):
    if board[idx] == ".":
        ans += "."
        idx += 1
    elif board[idx : idx + 4] == "XXXX":
        ans += "AAAA"
        idx += 4
    elif board[idx : idx + 2] == "XX":
        ans += "BB"
        idx += 2
    else:
        ans = -1
        break

print(ans)
