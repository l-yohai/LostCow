# https://www.acmicpc.net/problem/1158

import sys
from collections import defaultdict

n, k = list(map(int, sys.stdin.readline().split()))
#n, k = 7, 3
'''
원 초기화

더 간단히?
'''
circle = defaultdict(list)
circle[1].append(n)
for i in range(2, n + 1):
    circle[i].append(i - 1)
circle[n].append(1)
for i in range(n - 1, 0, -1):
    circle[i].append(i + 1)

josephus = []

pop_people = k  # k명에서 시작

for i in range(n):
    josephus.append(pop_people)
    prev, next = circle[pop_people]
    circle[prev][1] = next
    circle[next][0] = prev
    '''
    앞뒤 사람의 옆사람을 변경해줌
    '''
    for j in range(k):
        pop_people = next
        next = circle[pop_people][1]
        '''
        다음 k번 후 사람을 나아가며 찾음
        '''

josephus_permutation = ', '.join(list(map(str, josephus)))
print(f'<{josephus_permutation}>')
