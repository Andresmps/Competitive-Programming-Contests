import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))


a = read()

ls = read_line()

N, ls_ = ls[0], ls[1:]
mid_sum = math.ceil(sum(ls_) / 2)
print(mid_sum)
count_votes = {i:0 for i in ls_}

for i in range(2**N-1, -1, -1):
    bin_i = bin(i)[2::].zfill(N)[::-1] # Numero binario como string: 7 -> 111
    temp_set = []

    for j in range(len(bin_i)):

        if bin_i[j] == '1':
            temp_set.append(ls_[j])

    # print(temp_set)
    if sum(temp_set) >= mid_sum and 6 in temp_set:
        print(f"{i} : {bin_i}")
        print(f"{temp_set}")
        print(sum(temp_set))
        print(sum(set(ls_) - set(temp_set)))
        for k in set(temp_set):
            count_votes[k] = count_votes.get(k, 0) + 1
        

print(count_votes)