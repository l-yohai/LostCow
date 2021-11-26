import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

max_card = -1
for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            sum_card = cards[i] + cards[j] + cards[k]
            if sum_card <= m:
                max_card = max(max_card, sum_card)

print(max_card)
