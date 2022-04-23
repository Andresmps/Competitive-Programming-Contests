import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


a = read()

x = (2*a) / (a**2 + 1)
y = (2 - a*x)

# sum_ = (2*(a+1)) / (1 + a**2)

print(round(x + y, 5))
# print(round(sum_, 5))