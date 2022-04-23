import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

# print(sorted([ "CODE", "HELLO",  "HIM", "HI","HOME", "JAM"]))
# print(sorted([ "BBBB", "BBBBB",  "BBBBA", "BBBBC"]))
# print(sorted([ "PEEEL", "PEEEEEEL", "PEEE",  "PEEEA", "PEEEEEEA", "PEEEEEE"]))

t = read()

for t_ in range(t):

    str_ = input().strip()
    ls_str = []
    k, p = 0, 0

    while k < len(str_):

        ls_str.append(f"{str_[k]}_{p}")

        if k+1 >= len(str_):
            break

        if str_[k] != str_[k+1]:
            p += 1

        k += 1 

    ls_str.append(f"{chr(64)}_{1}")
    # print(ls_str)

    ls_str2 = []

    for i in ls_str:
        if i not in ls_str2:
            ls_str2.append(i)  

    # print(ls_str2) 

    count_str = {}
    for i in ls_str:
        count_str[i] = count_str.get(i, 0) + 1

    # print(count_str)

    ans = ""

    for i in range(len(ls_str2)-1):

        tmp_chr1 = ls_str2[i].split('_')[0]
        tmp_chr2 = ls_str2[i+1].split('_')[0]

        # print(tmp_chr1, count_str[ls_str2[i]])
        ans += tmp_chr1*count_str[ls_str2[i]]

        if ord(tmp_chr1) <= ord(tmp_chr2):
            ans += tmp_chr1*count_str[ls_str2[i]]

        # print(ans)
        # print()
    # ans += str_[-1]

    print(f"Case #{t_+1}: {ans}")



#     print()