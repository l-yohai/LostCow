import sys
import heapq

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

heap = []
heapq.heapify(heap)

for num in nums:
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -num)
