import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def validate_matrix_multi(N, rows_len, cols_len):

    matrix_dim = list(zip(rows_len, cols_len))
    print(f"Matrices dims: {matrix_dim}\n")

    for i in range(len(matrix_dim[:-1])):

        if matrix_dim[i][1] != matrix_dim[i+1][0]:
            return False

    return True

def numb_operations_two_matrices(A, B):

    colsA, colsB = len(A[0]), len(B[0])
    rowsA, rowsB = len(A), len(B)

    numb_oper = 0
    C = []

    for i in range(len(A)): # filas de A
        temp = []
        for j in range(len(B[0])): # columnas de B
            sum_ = 0
            for k in range(len(A[0])): # columnas de A
                sum_ += A[i][k] * B[k][j]
                numb_oper += 1

            temp.append(sum_)

        C.append(temp)

    print(f"A*B: {C}")
    print(numb_oper)
    print(rowsA * colsB * colsA)

    return numb_oper


def numb_operations_two_matrices_ordered(N, rows_len, cols_len, order_):

    matrix_dim = list(zip(rows_len, cols_len))
    print(f"Matrices dims: {matrix_dim}\n")
    numb_multi = 0

    for order_i in order_:
        print(order_i)
        dim_i1 = matrix_dim.pop(order_i-1)
        dim_i2 = matrix_dim[order_i-1]

        matrix_dim[order_i-1] = (dim_i1[0], dim_i2[1])

        print(f"dim_i1: {dim_i1}")
        print(f"dim_i2: {dim_i2}")
        print(f"# oper: {dim_i1[0] * dim_i2[1] * dim_i1[1]}")

        numb_multi += dim_i1[0] * dim_i2[1] * dim_i1[1]
        print(f"Reamining dims: {matrix_dim}")
        print()

    return numb_multi
    


# a)


N = 2 # read()
rows_len = [3, 2] # read_line()
cols_len = [2, 4] # read_line()

validate_matrix_multi_ = validate_matrix_multi(N, rows_len, cols_len)
print(f"Matrix multiplication can be made: {validate_matrix_multi_}\n\n")

# b)

A = [[1, 3], [2, 4], [2, 5]]
B = [[1, 3, 2, 2], [2, 4, 5, 1]]

print(f"A: {A}")
print(f"B: {B}\n")
print(f"Numb multiplications: {numb_operations_two_matrices(A, B)}\n\n")


# c)


N = 4 # read()
rows_len = [3, 2, 3, 3] # read_line()
cols_len = [2, 3, 4, 4] # read_line()
order_ = [2, 2, 1] # read_line()

validate_matrix_multi_2 = validate_matrix_multi(N, rows_len, cols_len)
print(f"Matrix multiplication can be made: {validate_matrix_multi_2}\n\n")

num_opera = numb_operations_two_matrices_ordered(N, rows_len, cols_len, order_)
print(num_opera)


 # a = [j for i in range(0, 10) for j in range(i, i+10)]
 # sum(a)