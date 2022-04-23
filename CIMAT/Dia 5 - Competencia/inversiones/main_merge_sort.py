import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]
 
    # print(L)
    # print(R)

    i, j, k, num_inv = 0, 0, l, 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            num_inv += j
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        num_inv += j
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return num_inv
 
 
def mergeSort(arr, l, r):

    num_inv = 0
    if r <= l:
        return num_inv
    
    m = l+(r-l)//2

    num_inv += mergeSort(arr, l, m)
    num_inv += mergeSort(arr, m+1, r)
    num_inv += merge(arr, l, m, r)
 
    return num_inv

N = read()
array = read_line()

num_inv = mergeSort(array, 0, N-1)

# print(array)
print(num_inv)
