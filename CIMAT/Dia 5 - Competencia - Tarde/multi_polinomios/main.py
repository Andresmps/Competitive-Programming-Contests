import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


T = read()

for _ in range(T):
    n, m = read_line()

    Ns = read_line()
    Ms = read_line()
    sol = [0 for i in range(n+m-1)]

    for i in range(n):
        for j in range(m):
            sol[i+j] += Ns[i] * Ms[j]
        # print(sol)

    print(" ".join([str(i) for i in sol]))

