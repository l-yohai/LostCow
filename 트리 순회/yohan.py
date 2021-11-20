import sys

input = sys.stdin.readline

n = int(input())


class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def preorder(node):
    print(node.value, end='')
    if node.left_child != '.':
        preorder(node.left_child)
    if node.right_child != '.':
        preorder(node.right_child)


def inorder(node):
    if node.left_child != '.':
        inorder(node.left_child)
    print(node.value, end='')
    if node.right_child != '.':
        inorder(node.right_child)


def postorder(node):
    if node.left_child != '.':
        postorder(node.left_child)
    if node.right_child != '.':
        postorder(node.right_child)
    print(node.value, end='')


tree = []
for _ in range(n):
    curr, left_child, right_child = map(str, input().strip().split())
    node = Node(curr, left_child, right_child)
    tree.append(node)

for i in range(n):
    for j in range(n):
        if tree[i].value == tree[j].left_child:
            tree[j].left_child = tree[i]
        elif tree[i].value == tree[j].right_child:
            tree[j].right_child = tree[i]

preorder(tree[0])
print()
inorder(tree[0])
print()
postorder(tree[0])
print()
