import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


t = read()

for t_ in range(t):
    
    ls1, ls2, ls3 = read_line(), read_line(), read_line()
    ls4 = []
    total = 10**6

    for i, j, k in zip(ls1, ls2, ls3):
        ls4.append(min(i, j, k))


    if sum(ls4) < total:
        print(f"Case #{t_+1}: IMPOSSIBLE")
    else:

        c, m, y, k = 0, 0, 0, 0

        if total <= ls4[0]:
            c = total
        else:
            total -= ls4[0]
            c = ls4[0]

            if total <= ls4[1]:
                m = total
            else:
                total -= ls4[1]
                m = ls4[1]

                if total <= ls4[2]:
                    y = total
                else:
                    total -= ls4[2]
                    y = ls4[2]

                    if total <= ls4[3]:
                        k = total 
                    else:
                        total -= ls4[3]
                        k = ls4[3]

        print(f"Case #{t_+1}: {c} {m} {y} {k}")