N = int(input())

li = [0,1,1] + [None]*20
def func(N):
    if li[N] != None:
        return li[N]
    else:
        li[N] = func(N-1) + func(N-2)
        return li[N]
print(func(N))