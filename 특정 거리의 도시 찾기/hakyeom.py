import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, k, x = list(map(int, input().split()))

city_map = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    city_map[i].append(j)

# print(city_map)

cnt_length = defaultdict(int)


start_city = x
q = deque()
for next in city_map[x]:
    q.append((start_city, next))

while q:
    start, next = q.popleft()

    if not next in cnt_length:
        cnt_length[next] = cnt_length[start] + 1

        for n in city_map[next]:
            q.append((next, n))

    else:
        if cnt_length[start] + 1 <= cnt_length[next]:
            cnt_length[next] = cnt_length[start] + 1
            for n in city_map[next]:
                q.append((next, n))

# print(cnt_length) # aa

len_city_dict = defaultdict(list)

for city, length in cnt_length.items():
    len_city_dict[length].append(city)

len_city_dict[k].sort()
if not len_city_dict[k]:
    print(-1)
else:
    for city in len_city_dict[k]:
        print(city)
