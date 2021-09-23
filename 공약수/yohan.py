n = int(input())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


if n == 2:
    a, b = map(int, input().split())
    g = gcd(a, b)
else:
    a, b, c = map(int, input().split())
    g = gcd(a, gcd(b, c))

for i in range(1, g + 1):
    if g % i == 0:
        print(i)
