import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def get_numb_operations(A):
    operations = 0

    for i in range(len(A)):
        for j in range(len(A[i])):

            max_value = A[i][j]

            if i != 0:
                max_value = max(max_value, A[i-1][j] + 1)

            if j != 0:
                max_value = max(max_value, A[i][j-1] + 1)

            operations += max_value - A[i][j]
            A[i][j] = max_value
            

            # print(A[i][j])
            # print()

    return operations


n, m = read_line()
A = []

for _ in range(n):
    A.append(read_line())

operations = get_numb_operations(A)

print(operations)
# print("El valor max de la función sería 10*10*10^4 + E_{i=0}^{9} E_{j=i}^{i+9} j = 10^6^+ 9 * 10^2")
# print("No, dado que operations > 10*10*10^4 que supera el limite superior de una variable de 16bit (approx 2^15).")
# print(A)