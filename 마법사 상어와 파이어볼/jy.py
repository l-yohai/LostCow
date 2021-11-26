N, M, K = map(int, input().split())

fbs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r = r - 1
    c = c - 1
    fbs.append([r, c, m, s, d])

dd = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    visit = [[[] for _ in range(N)] for _ in range(N)]
    cors = set()
    while fbs:
        r, c, m, s, d = fbs.pop()
        r = (r + dd[d][0] * s) % N
        c = (c + dd[d][1] * s) % N
        visit[r][c].append((m, s, d))
        cors.add((r, c))

    for r, c in cors:
        if len(visit[r][c]) > 1:
            p_fbs = visit[r][c]
            ms, ss, ds = zip(*p_fbs)
            m = sum(ms) // 5
            if m == 0:
                continue
            s = sum(ss) // len(ss)
            tds = list(map(lambda x: True if x % 2 == 1 else False, ds))
            if tds == [False] * len(visit[r][c]) or tds == [True] * len(visit[r][c]):
                ds = [0, 2, 4, 6]
            else:
                ds = [1, 3, 5, 7]
            for d in ds:
                fbs.append((r, c, m, s, d))

        else:
            m, s, d = visit[r][c][0]
            fbs.append((r, c, m, s, d))
if fbs:
    rs, cs, ms, ss, ds = zip(*fbs)
    print(sum(ms))
else:
    print(0)
