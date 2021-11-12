# https://www.acmicpc.net/problem/3029
import sys

input = sys.stdin.readline

cur_t = input().strip()
pln_t = input().strip()


def to_sec(str_time):
    hh, mm, ss = str_time.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def to_hour(sec):
    hh = sec // 3600
    ss = sec % 3600
    mm = ss // 60
    ss = ss % 60

    return f"{hh:02}:{mm:02}:{ss:02}"


cur_t = to_hour(to_sec(cur_t))
pln_t = to_hour(to_sec(pln_t))

if pln_t > cur_t:
    print(to_hour(to_sec(pln_t) - to_sec(cur_t)))
else:
    print(to_hour(to_sec("24:00:00") - to_sec(cur_t) + to_sec(pln_t)))
