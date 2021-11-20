import sys
from collections import defaultdict

# https://jjangsungwon.tistory.com/12


class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    print(node.item, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])


def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != ".":
        inorder(tree[node.right])


def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.item, end="")


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    preorder(tree["A"])
    print()
    inorder(tree["A"])
    print()
    postorder(tree["A"])

    # 클래스를 만드는 것을 두려워 하지 말것
