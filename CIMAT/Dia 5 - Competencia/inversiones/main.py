import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


N = read()
array = read_line()

numb_com = 0

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            numb_com += 1

print(numb_com) 

