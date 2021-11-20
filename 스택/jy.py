from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
stack = deque()
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(cmd[1])
        continue
    cmd = cmd[0]
    if cmd == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
