from itertools import permutations

N, M = map(int, input().split())
ans = list(permutations(range(1, N+1), M))

for i in ans:
    print(' '.join(map(str, i)))