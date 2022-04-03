import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())


t = read()

for _ in range(t):
    p, q, n = read_line()

    array_sums = [(p*i) % q for i in range(1, q+1)]
    print(p, q, n)
    print(array_sums)
    num_cycles = math.floor(n/q)
    incomplete_cycle = n % q

    print(num_cycles, incomplete_cycle)
    ans = int((((q * (q-1)) / 2) * num_cycles) + sum(array_sums[:incomplete_cycle]))

    print(ans)
    print()
