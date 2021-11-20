import sys
from collections import deque

n = int(input())

command = []
for _ in range(n):
    command.append(sys.stdin.readline().strip())

stack = deque()
for c in command:
    if c.startswith('push'):
        stack.append(c.split()[-1])
    elif c == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif c == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
