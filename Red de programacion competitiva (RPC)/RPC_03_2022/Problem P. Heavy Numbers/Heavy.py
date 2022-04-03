import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())


def get_weight(x):
    num_digs = len(str(x))
    sum_digs = sum(map(int, list(str(x))))

    return num_digs*sum_digs

a, b = read_line()
w_a, w_b = get_weight(a), get_weight(b)

if w_a == w_b:
    print(0)
else:
    print(1 if w_a > w_b else 2)


