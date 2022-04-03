import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


def recursive_count(nj, i):

    # print(nj, i)
    if i >= len(ls):
        return 0

    if ls[i] < nj:
        return 0

    # if d_array[i][nj] != -1:
    #     return d_array[i][nj]

    # d_array[i][nj] = recursive_count(nj+1, i+1)
    count_ = recursive_count(nj+1, i+1)

    # return d_array[i][nj] + 1
    return count_ + 1


def fill_d_array(N):
    return [
        [-1 for _ in range(10**6 + 1)] # 
        for _ in range(N+1)
    ]


t = read()

for t_ in range(t):
    
    N = read()
    ls = sorted(read_line())

    # print(ls)

    # d_array = fill_d_array(N)
    max_count = 0

    for i in range(len(ls)):
        for nj in range(1, ls[i]+1):
            # print(nj, i, ls[i])
            count_ = recursive_count(nj, i)
            # print('count:', count_, '\n')
            max_count = max(max_count, count_)

    print(f"Case #{t_+1}: {max_count}")

    


