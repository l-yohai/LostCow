n = int(input())
li = list(map(int, input().split()))
ans = 0
s = sum(li)
for num in li[:-1]:
    s -= num
    ans += num*s

print(ans)
