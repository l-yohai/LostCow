n = int(input())

arr = list(map(int, input().split()))
cf = []

def gcd(a, b):
    if a==0:
        return b
    return gcd(b % a, a)
    
g = gcd(arr[0], gcd(arr[1], arr[-1]))
for i in range(1, (g//2)+1):
    if g%i ==0:
        print(i)
print(g)
