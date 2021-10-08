N, M = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx_a = 0
idx_b = 0

ans = []
while idx_a != N and idx_b != M:
    if arr_a[idx_a] <= arr_b[idx_b]:
        ans.append(arr_a[idx_a])
        idx_a += 1
    else:
        ans.append(arr_b[idx_b])
        idx_b += 1
if idx_a != N:
    ans.extend(arr_a[idx_a:])
else:
    ans.extend(arr_b[idx_b:])

print(' '.join(map(str, ans)))
