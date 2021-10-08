import sys
input = sys.stdin.readline

N = int(input())
favorite_info = {}

for i in range(N*N):
    info = list(map(int, input().split()))
    favorite_info[info[0]] = info[1:]
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class_room = [[0]*N for _ in range(N)]

# N = 3
# favorite_info = {4: [2, 5, 1, 7], 3: [1, 9, 4, 5], 9: [8, 1, 2, 3], 8: [1, 9, 3, 4], 7: [
#     2, 3, 4, 8], 1: [9, 2, 5, 7], 6: [5, 2, 3, 4], 5: [1, 9, 2, 8], 2: [9, 3, 1, 4]}

#
# class_room = [[0]*N for _ in range(N)]


def get_favorite_num(class_room, student):
    favorite_list = favorite_info[student]

    favorite_cnt_map = [[0]*N for _ in range(N)]
    for y in range(len(class_room)):

        for x in range(len(class_room[y])):
            if class_room[y][x] == 0:  # 비어있고
                favorite_cnt = 0
                for dy, dx in DIR:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if class_room[ny][nx] in favorite_list:
                            favorite_cnt += 1

                favorite_cnt_map[y][x] = favorite_cnt
    return favorite_cnt_map


def get_blank_num(class_room):

    blank_cnt_map = [[-1]*N for _ in range(N)]
    for y in range(len(class_room)):

        for x in range(len(class_room[y])):
            if class_room[y][x] == 0:  # 비어있고
                blank_cnt = 0
                for dy, dx in DIR:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if class_room[ny][nx] == 0:
                            blank_cnt += 1

                blank_cnt_map[y][x] = blank_cnt
    return blank_cnt_map


def fill_class_room(class_room, blank_num_map, blank_max, student_num, points):
    for y in range(len(blank_num_map)):
        for x in range(len(blank_num_map[y])):
            if blank_num_map[y][x] == blank_max and [y, x] in points:
                class_room[y][x] = student_num
                return


def get_favorite_score(class_room):

    favorite_cnt_map = [[0]*N for _ in range(N)]
    for y in range(len(class_room)):

        for x in range(len(class_room[y])):

            favorite_cnt = 0
            for dy, dx in DIR:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if class_room[ny][nx] in favorite_info[class_room[y][x]]:
                        favorite_cnt += 1

            favorite_cnt_map[y][x] = favorite_cnt
    return favorite_cnt_map


for i in favorite_info.keys():
    # print(i)
    favorite_num_map = get_favorite_num(class_room, i)
    # print()
    # for f in favorite_num_map:
    #     print(f)
    # print()

    '''
    좋아하는 사람이 많은 수를 찾음
    row_max
    '''
    row_max = 0
    for y in range(len(favorite_num_map)):
        row_max = max(max(favorite_num_map[y]), row_max)

    points = []
    for y in range(len(favorite_num_map)):

        for x in range(len(favorite_num_map[y])):
            if row_max == favorite_num_map[y][x]:
                points.append([y, x])
    # print(points)

    blank_num_map = get_blank_num(class_room)
    # print()
    # for bn in blank_num_map:
    #     print(bn)
    # print()
    blank_max = blank_num_map[points[0][0]][points[0][1]]

    if len(points) >= 1:
        for y, x in points[1:]:
            blank_max = max(blank_max, blank_num_map[y][x])

    fill_class_room(class_room, blank_num_map, blank_max, i, points)

    # for c in class_room:
    #     print(c)

    # print()
# print(class_room)
score_map = get_favorite_score(class_room)
for i in favorite_info.keys():

    score = 0

    for y in range(len(score_map)):
        for x in range(len(score_map[y])):
            fav_num = score_map[y][x]
            if fav_num == 0:
                score += 0
            elif fav_num == 1:
                score += 1
            elif fav_num == 2:
                score += 10
            elif fav_num == 3:
                score += 100
            else:
                score += 1000
print(score)
