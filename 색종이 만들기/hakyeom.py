# https://www.acmicpc.net/problem/2630
import sys
from collections import deque, defaultdict
from pprint import pprint

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


def check(paper):
    """
    같은 색인지 검사하는 메서드
    """
    if len(paper) == 1:
        return True
    else:
        color = paper[0][0]
        for y in range(len(paper)):
            for x in range(len(paper[y])):
                if color != paper[y][x]:
                    return False

    return True


def split_paper(paper):
    half_len = len(paper) // 2
    upper_paper = paper[:half_len]
    bottom_paper = paper[half_len:]

    uppper_left = [upper[:half_len] for upper in upper_paper]
    uppper_right = [upper[half_len:] for upper in upper_paper]
    bottom_left = [bottom[:half_len] for bottom in bottom_paper]
    bottom_right = [bottom[half_len:] for bottom in bottom_paper]

    return [uppper_left, uppper_right, bottom_left, bottom_right]


def count_color(paper):
    color = paper[0][0]
    return color, len(paper) * len(paper)


q = deque([paper])
count = defaultdict(int)
while q:
    paper = q.popleft()

    if not check(paper):
        splited_papers = split_paper(paper)
        for p in splited_papers:
            q.append(p)
    else:
        color, cnt = count_color(paper)
        count[color] += 1

print(count[0])
print(count[1])
