import sys

input = sys.stdin.readline
n, m = map(int, input().split())

set_list = [i for i in range(n + 1)]


def get_parent(li, num):
    if li[num] == num:
        return num
    return get_parent(li, li[num])


def union(li, num1, num2):
    num1 = get_parent(li, num1)
    num2 = get_parent(li, num2)
    li[min(num1, num2)] = max(num1, num2)


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(set_list, a, b)
    if op == 1:
        a = get_parent(set_list, a)
        b = get_parent(set_list, b)
        if a == b:
            print("YES")
        else:
            print("NO")

# https://m.blog.naver.com/ndb796/221230967614
