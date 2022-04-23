import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


cakes = list(input().strip())
k = read()
count = 0
print(cakes)
for i in range(len(cakes)):

    if cakes[i] == '-':
        count += 1
        for j in range(k):
            if i+j < len(cakes):
                cakes[i+j] = '-' if cakes[i+j] == '+' else '+'
        print(cakes)
print(count)