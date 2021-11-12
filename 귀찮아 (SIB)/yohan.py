n = int(input())
m = list(map(int, input().split()))

num = []
num.append(m[0])

for i in range(n - 1):
    num.append(num[i] + m[i + 1])

answer = 0
for i in range(n):
    answer += m[i] * (num[n - 1] - num[i])

print(answer)
