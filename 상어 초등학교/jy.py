N = int(input())

prefer_dict = dict()
for _ in range(N**2):
    st_num, *li = map(int, input().split())
    li = set(li)
    prefer_dict[st_num] = li

_class = [[None]*N for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

empty_seats = set((i, j) for i in range(N) for j in range(N))
for st_num in prefer_dict:
    max_pref_st = 0
    seats = []

    for empty_seat in empty_seats:
        r, c = empty_seat
        pref_st = 0
        null_cnt = 0

        for i, j in d:
            if 0 <= r+i < N and 0 <= c+j < N:
                if _class[r+i][c+j] == None:
                    null_cnt += 1
                elif _class[r+i][c+j] in prefer_dict[st_num]:
                    pref_st += 1

        if max_pref_st == pref_st:
            seats.append((r, c, null_cnt, ))
        elif pref_st > max_pref_st:
            seats = []
            seats.append((r, c, null_cnt, ))
            max_pref_st = pref_st

    seats.sort(key=lambda x: x[1])
    seats.sort(key=lambda x: x[0])
    seats.sort(key=lambda x: x[2], reverse=True)

    r, c, *_ = seats[0]
    _class[r][c] = st_num

    empty_seats.remove((r, c))

ans = 0
for r in range(N):
    for c in range(N):
        pref_cnt = 0
        for i, j in d:
            if 0 <= r+i < N and 0 <= c+j < N and _class[r+i][c+j] in prefer_dict[_class[r][c]]:
                pref_cnt += 1
        ans += 10**(pref_cnt-1) if pref_cnt != 0 else 0
print(ans)
