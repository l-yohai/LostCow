# https://www.acmicpc.net/problem/11728
import sys

'''
input
배열 A의 크기 N, 배열 B의 크기 M
배열 A
배열 B
'''

input = sys.stdin.readline
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

'''
배열 A의 idx
배열 B의 idx
'''
a_idx = 0
b_idx = 0

'''
배열의 두 값을 비교하여 작은 값을 nums에 추가
추가된 배열의 인덱스값을 +1 해준다.
두 인덱스 중 하나가 끝까지 가면 while을 종료
'''
nums = []
while a_idx < N and b_idx < M:

    if A[a_idx] >= B[b_idx]:
        nums.append(B[b_idx])
        b_idx += 1
    else:
        nums.append(A[a_idx])
        a_idx += 1

'''
정렬된 배열 A,B가 주어지므로 아직 탐색 못한 배열은
nums[-1] 보다 큰 숫자들이므로 extend 해준다.
'''

if a_idx == N:
    nums.extend(B[b_idx:])
else:
    nums.extend(A[a_idx:])

for num in nums:
    print(num, end=' ')
