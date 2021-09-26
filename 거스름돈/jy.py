n = int(input())
f_coin = n//5

while f_coin>-1:
    if (n-f_coin*5)%2==0:
        print(f_coin+(n-5*f_coin)//2)
        exit()
    else:
        f_coin -= 1
print(-1)