# https://www.acmicpc.net/problem/10870
import sys

n = int(sys.stdin.readline())

fibo_seq = {0: 0,
            1: 1}


def fibonaci(idx):
    if idx in fibo_seq.keys():
        return fibo_seq[idx]
    else:
        fibo_seq[idx] = fibonaci(idx - 1) + fibonaci(idx - 2)
        return fibo_seq[idx]


print(fibonaci(n))
