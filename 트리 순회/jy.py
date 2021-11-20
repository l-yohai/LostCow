class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def insert_left(self, node, lnode):
        r = self.root
        node = self.search(r, node.item)
        node.left = lnode

    def insert_right(self, node, rnode):
        r = self.root
        node = self.search(r, node.item)
        node.right = rnode

    def search(self, cur, srch: str):
        if cur:
            if cur.item == srch:
                return cur
            a = self.search(cur.left, srch)
            b = self.search(cur.right, srch)
            if a:
                return a
            else:
                return b
        else:
            return None

    def preorder_traversal(self, node):
        if node:
            print(node.item, end="")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.item, end="")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.item, end="")


N = int(input())
a, b, c = input().split()
anode = Node(a)
tt = Tree(anode)
if b != ".":
    bnode = Node(b)
    tt.insert_left(anode, bnode)
if c != ".":
    cnode = Node(c)
    tt.insert_right(anode, cnode)

for _ in range(N - 1):
    a, b, c = input().split()
    anode = Node(a)
    if b != ".":
        bnode = Node(b)
        tt.insert_left(anode, bnode)
    if c != ".":
        cnode = Node(c)
        tt.insert_right(anode, cnode)

tt.preorder_traversal(tt.root)
print()
tt.inorder_traversal(tt.root)
print()
tt.postorder_traversal(tt.root)
