import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


T = read()

for _ in range(T):
    str_ = input().strip()

    mid = int(len(str_)//2)
    print("SI" if str_[:mid] == str_[::-1][:mid] else "NO")
    