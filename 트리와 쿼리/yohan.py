import sys
sys.setrecursionlimit(10**9)


n, r, q = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

sub_trees = [0] * (n + 1)


def count_subtree_nodes(curr):
    sub_trees[curr] = 1
    for t in tree[curr]:
        if not sub_trees[t]:
            count_subtree_nodes(t)
            sub_trees[curr] += sub_trees[t]


count_subtree_nodes(r)

for i in range(q):
    u = int(sys.stdin.readline())
    print(sub_trees[u])
