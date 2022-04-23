import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


def determinante(A):
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    deter_ = 0

    for k in range(len(A)):
        temp_A = [
            [
                A[i][j] for j in range(len(A)) if j != k 
            ] for i in range(1, len(A[0])) 
        ]

        # print(temp_A)
        deter_ += A[0][k] * (-1)**(k) * determinante(temp_A)
        # print(A[0][k] * (-1)**(k+1) * determinante(temp_A))
        # print()

    return deter_


T = read()

A = [read_line() for _ in range(T)]

# print(A)

print(determinante(A))


# A = [
#     [3, 5, 2],
#     [4, 2, 3],
#     [-1, 2, 4]
# ]

# print(determinante(A))
# [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ]

# print([[A[i][j] for j in range(len(A)) if j != 1] for i in range(1, len(A[0])) ])