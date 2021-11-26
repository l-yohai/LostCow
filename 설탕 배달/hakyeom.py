import sys

input = sys.stdin.readline

n = int(input().strip())

arr = [5001] * (n + 5)
arr[3] = arr[5] = 1

for i in range(6, n + 1):
    arr[i] = min(arr[i - 3], arr[i - 5]) + 1

print(arr[n] if arr[n] < 5001 else -1)

# dp
# 이중포문으로도 풀림
# i-3과 i-5에는 계속 최솟값만 저장
# 최솟값 + 최솟값 = 최솟값
# 두개의 값중 작은 것을 선택
