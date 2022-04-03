import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())

def find_U(x):
    for i in range(len(x)):
        if x[i] == 'U':
            return i

def find_F(x):
    for i in range(len(x)):
        if x[len(x)-i-1] == 'F':
            return len(x)-i-1

str_ = input().strip()
find_u = find_U(str_)
find_f = find_F(str_)
find_c = find_f - find_u - 1

ans = '-'*(find_u) + 'U' + 'C'*(find_c) + 'F' + '-'*(len(str_) - find_f - 1) 

print(ans)


