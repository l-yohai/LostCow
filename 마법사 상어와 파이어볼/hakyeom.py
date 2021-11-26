import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

fire_ball_infos = []

# n = 10


def move(dir, ri, ci, si):
    nri, nci = ri, ci
    if dir == 0:
        nri += si
    elif dir == 1:
        nri += si
        nci += si
    elif dir == 2:
        nci += si
    elif dir == 3:
        nri -= si
        nci += si
    elif dir == 4:
        nri -= si
    elif dir == 5:
        nri -= si
        nci -= si
    elif dir == 6:
        nci -= si
    elif dir == 7:
        nri += si
        nci -= si

    if nci > n:
        nci = nci % n
        if nci == 0:
            nci += 1

    if nri > n:
        nri = nri % n
        if nri == 0:
            nri += 1
    # 음수이동 추가

    return nri, nci


for _ in range(m):
    fire_ball_infos.append(list(map(int, input().split())))
    # ri,ci,mi,si,di = map(int,input().split())

point_fire = defaultdict(list)
loop = 0
for _ in range(k):
    if loop == 0:
        for fire_ball_info in fire_ball_infos:
            ri, ci, mi, si, di = fire_ball_info

            nri, nci = move(di, ri, ci, si)
            point_fire[(nri, nci)].append([nri, nci, mi, si, di])
        loop += 1
    else:
        points = list(point_fire.keys())
        for point in points:
            for i in range(len(point_fire[point])):
                ri, ci, mi, si, di = point_fire[point][i]
                nri, nci = move(di, ri, ci, si)
                point_fire[(nri, nci)].append([nri, nci, mi, si, di])
        point_fire.pop(point)
        loop += 1

    is_all_one = True
    points = list(point_fire.keys())
    for point in points:
        if len(point_fire[point]) != 1:
            is_all_one = False

    while not is_all_one:
        points = list(point_fire.keys())
        # print(points)
        # temp_dict = defaultdict(list)
        for point in points:
            sri, sci, smi, ssi, sdi = 0, 0, 0, 0, 0
            if len(point_fire[point]) != 1:
                total = len(point_fire[point])
                for info in point_fire[point]:
                    ri, ci, mi, si, di = info
                    smi += mi
                    ssi += si
                # print(smi)
                smi = smi // 5
                # print(smi)
                ssi = ssi // total
                point_fire.pop(point)
                if smi != 0:
                    if total % 2 == 0:
                        ri1, ci1 = move(0, ri, ci, 0)
                        ri2, ci2 = move(2, ri, ci, 0)
                        ri3, ci3 = move(4, ri, ci, 0)
                        ri4, ci4 = move(6, ri, ci, 0)
                        point_fire[(ri1, ci1)].append([ri1, ci1, smi, ssi, 0])
                        point_fire[(ri2, ci2)].append([ri2, ci2, smi, ssi, 2])
                        point_fire[(ri3, ci3)].append([ri3, ci3, smi, ssi, 4])
                        point_fire[(ri4, ci4)].append([ri4, ci4, smi, ssi, 6])
                    else:
                        ri1, ci1 = move(1, ri, ci, 0)
                        ri2, ci2 = move(3, ri, ci, 0)
                        ri3, ci3 = move(5, ri, ci, 0)
                        ri4, ci4 = move(7, ri, ci, 0)
                        point_fire[(ri1, ci1)].append([ri1, ci1, smi, ssi, 1])
                        point_fire[(ri2, ci2)].append([ri2, ci2, smi, ssi, 3])
                        point_fire[(ri3, ci3)].append([ri3, ci3, smi, ssi, 5])
                        point_fire[(ri4, ci4)].append([ri4, ci4, smi, ssi, 7])
        break

        # else:
        #     temp_dict[point] = point_fire[point]
        # is_all_one = True
        # points = list(point_fire.keys())
        # for point in points:
        #     if len(point_fire[point]) != 1:
        #         is_all_one = False
    print(point_fire)

points = list(point_fire.keys())
ans = 0
# print(point_fire)
for point in points:
    ans += point_fire[point][0][2]
print(ans)
