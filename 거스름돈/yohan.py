n = int(input())

answer, count = 0, 0

if n < 5:
    if n % 2 != 0:
        answer = -1
    else:
        answer = n // 2
else:
    count = n // 5
    n %= 5

    if n == 0:
        answer = count
    else:
        if n % 2 == 0:
            count += n // 2
        else:
            count += (n + 5) // 2 - 1
        answer = count

print(answer)
