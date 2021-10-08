import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def dfs(num, numbers, result):
    result.append(num)
    numbers.remove(num)

    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    else:
        for n in numbers:
            dfs(n, numbers[:], result[:])


numbers = list(range(1, N + 1))

for num in numbers:
    dfs(num, numbers[:], [])
