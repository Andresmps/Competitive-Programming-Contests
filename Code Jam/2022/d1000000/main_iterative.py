import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


t = read()

for t_ in range(t):
    
    N = read()
    ls = sorted(read_line())

    max_count = 0
    i = 0

    for nj in range(1, N+1):
        while i < len(ls):
            if ls[i] >= nj:
                max_count += 1
                i += 1
                break
            i += 1

    print(f"Case #{t_+1}: {max_count}")
