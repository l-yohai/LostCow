a = int(input())

max5num = a // 5

com = False
for num5 in reversed(range(max5num + 1)):
    num3 = (a - num5 * 5) // 3

    if num5 * 5 + num3 * 3 == a:
        print(num5 + num3)
        com = True
        break

if com is False:
    print(-1)
