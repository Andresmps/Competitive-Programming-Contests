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

            print(A[i][j])

            val_top, val_left = -1, -1

            if i != 0 and A[i-1][j] > A[i][j]:
                val_top = A[i-1][j]

            if j != 0 and A[i][j-1] > A[i][j]:
                val_left = A[i][j-1]

            if val_top == -1 and val_left == -1:
                print()
                continue

            max_val = max(val_left, val_top)
            print(max_val)
            operations += max_val - A[i][j] + 1
            A[i][j] += max_val - A[i][j] + 1
            

            print(A[i][j])
            print()

    return operations


n, m = read_line()
A = []

10000 + 10001 + 10002
10001 + 10002 + 10003
10002 + 10003 + 10004

for _ in range(n):
    A.append(read_line())

operations = get_numb_operations(A)

print(f"# operations = {operations}")
print("El valor max de la función sería 10*10*10^4 + E_{i=0}^{9} E_{j=i}^{i+9} j = 10^6^+ 9 * 10^2")
print("No, dado que operations > 10*10*10^4 que supera el limite superior de una variable de 16bit (approx 2^15).")
print(A)