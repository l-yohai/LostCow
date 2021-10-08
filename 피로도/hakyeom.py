import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())

"""
하루에 한 시간 단위로 일을 하거나 일을 쉬어도 된다. 하루에 한 시간 일하면 피로도는 $A$ 만큼 쌓이고 일은 $B$ 만큼 처리할 수 있다.

만약에 한 시간을 쉰다면 피로도는 $C$ 만큼 줄어든다. 단, 피로도는 절대 0보다 작아질 수 없다. 당연히 일을 하지 않고 쉬었기 때문에 처리한 일은 없다.

피로도를 최대한 $M$ 을 넘지 않게 일을 하려고 한다.
"""

work = 0
cur = 0
loop = 0
while loop < 24:
    loop += 1
    if cur + A <= M:
        cur += A
        work += B
    else:
        cur -= C
        cur = cur if cur >= 0 else 0

print(work)
