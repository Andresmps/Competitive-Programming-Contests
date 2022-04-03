import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


t = read()

for t_ in range(t):

    R, C = read_line()
    ls = "\n".join(
        [ 
            "".join(
                [
                    "." if i in [0, 1] and j == 0 else "."
                    if i == 0 and j == 1 else "+"
                    if i % 2 == 0 and j % 2 == 0 else "-"
                    if i % 2 == 0 and j % 2 != 0 else "."
                    if i % 2 != 0 and j % 2 != 0 else "|"
                     for j in range(C*2 + 1)
                ]
            ) for i in range(R*2 + 1)
        ]
    )

    print(f"Case #{t_+1}:")
    print(ls)