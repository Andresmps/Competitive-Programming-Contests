import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


N = read()

sum_ = int((N*(N+1))/2)

print(sum_)