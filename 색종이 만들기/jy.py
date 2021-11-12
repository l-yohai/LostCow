import sys
input = sys.stdin.readline
li = []
N = int(input())
blue_num = 0
white_num = 0

def func(li, n):
    global blue_num
    global white_num
    if '1' not in str(li):
        white_num += 1
        return
    if '0' not in str(li):
        blue_num += 1
        return
    li1, li2, li3, li4 = [], [], [], []
    i = 0
    while i<n//2:
        li1.append(li[i][:n])
        li2.append(li[i][n:])
        li3.append(li[n//2+i][:n])
        li4.append(li[n//2+i][n:])
        i += 1
    func(li1, n//2)
    func(li2, n//2)
    func(li3, n//2)
    func(li4, n//2)

for _ in range(N):
    li.append(input())
func(li, N)

print(white_num)
print(blue_num)
