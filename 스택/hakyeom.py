import sys


class Node:
    def __init__(self, num):
        self.num = num
        self.pre = None

    def previous(self, pre):
        self.pre = pre


class Stack:
    def __init__(self):
        self.node = None
        self.stack_size = 0

    def push(self, num):
        temp = Node(num)
        temp.previous(self.node)
        self.node = temp
        self.stack_size += 1

    def pop(self):
        if self.node:
            rtn = self.node.num
            self.node = self.node.pre
            self.stack_size -= 1
        else:
            rtn = -1
        return rtn

    def size(self):
        return self.stack_size

    def empty(self):
        size = self.size()
        if size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.node:
            rtn = self.node.num
        else:
            rtn = -1
        return rtn


input = sys.stdin.readline

n = int(input().strip())
stack = Stack()

for _ in range(n):
    cmd = input().split()
    method = cmd[0]

    if method == "push":
        stack.push(int(cmd[1]))
    elif method == "pop":
        num = stack.pop()
        print(num)
    elif method == "top":
        print(stack.top())
    elif method == "size":
        print(stack.size())
    elif method == "empty":
        print(stack.empty())
