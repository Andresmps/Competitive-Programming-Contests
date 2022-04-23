import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def val_intercept_subsets(set_):

    set_ = sorted(set_, key=lambda x: x[0])

    for i in range(len(set_[:-1])):
        if set_[i][1] > set_[i+1][0]:
            return False

    return True

def find_max_set(N, set_):

    max_len = 0

    for i in range(2**N-1, -1, -1):
        bin_i = bin(i)[2::].zfill(N)[::-1] # Numero binario como string: 7 -> 111
        temp_set = []

        print(f"{i} : {bin_i}")

        for j in range(len(bin_i)):

            if bin_i[j] == '1':
                temp_set.append(set_[j])

        print(f"{temp_set}")
        is_valid = val_intercept_subsets(temp_set)

        if is_valid:
            max_len = max(max_len, len(temp_set))
            # break


    return max_len


N = 3 # read()
# set_ = [(1, 4), (3, 6), (5, 8)] # read_line()
# set_ = [(1, 4), (5, 8)] # read_line()
set_ = [(2, 4), (6, 8), (1, 20)]


print(val_intercept_subsets(set_))
print(f"Length bigger subset without interceptions: {find_max_set(N, set_)}")


