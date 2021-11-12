# https://www.acmicpc.net/problem/1197
import sys

input = sys.stdin.readline


def get_parent(li, child):
    if li[child] == child:
        return child
    else:
        return get_parent(li, li[child])


def union(li, num1, num2):
    num1 = get_parent(li, num1)
    num2 = get_parent(li, num2)
    li[min(num1, num2)] = max(num1, num2)


v, e = map(int, input().split())
tree = list(range(v + 1))
node_info = []

for _ in range(e):
    a, b, c = map(int, input().split())
    node_info.append([a, b, c])

node_info.sort(key=lambda x: x[2])

ans = 0
for a, b, c in node_info:
    if get_parent(tree, a) != get_parent(tree, b):
        union(tree, a, b)
        ans += c
print(ans)
