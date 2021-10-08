# https://www.acmicpc.net/problem/5618
import sys

'''
입력
'''
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

'''
가장 큰 숫자를 찾고
그 숫자의 약수들을 찾음
'''
max_divisors = []
max_number = max(numbers)

for divisor in range(1, int(max_number ** 0.5) + 1):
    if max_number % divisor == 0:
        max_divisors.append(divisor)

for divisor in max_divisors[::-1]:
    max_divisors.append(max_number // divisor)

'''
6 ->
1, 2
6//1, 6// 2


제곱근이 나눠 떨어지는 경우 ex) 4
위의 로직에서는 max_divisor가 1,2,2,4 가 나오게된다.
중복을 없애기 위해 set으로 변경
set으로 변경 할 때 순서가 유지 되지 않는 경우가 있으므로 sort를 해줘서
작은 수부터 출력 가능하게 만든다.
'''

max_divisors = list(set(max_divisors))
max_divisors.sort()
'''
가장 큰 숫자의 약수들 중에서 공약수를 찾는다.
'''
result = []
for divisor in max_divisors:
    for num in numbers:
        if num % divisor != 0:
            break
    else:
        print(divisor)
