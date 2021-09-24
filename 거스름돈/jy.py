n = int(input())
f_coin = n//5

while True:
    if (n-f_coin*5)%2==0:
        print(f_coin+(n-5*f_coin)//2)
        break
    else:
        f_coin -= 1