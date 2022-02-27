import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())

n, k = read_line()
ls = [read() for _ in range(n)]
dict_count = {}
sort_ls = []
marks = [False for i in range(2*10**5)]

for i in range(n):
    dict_count[ls[i]] = dict_count.get(ls[i], 0) + 1

# print(n, k)
# print(dict_count)

sort_ls.append(ls[0])
dict_count[ls[0]] -= 1
marks[ls[0]] = True


for i in range(1, n):
    
    dict_count[ls[i]] -= 1

    if marks[ls[i]] == True:
        continue
    
    marks[ls[i]] = True

    while len(sort_ls) > 0 and sort_ls[-1] > ls[i] and dict_count[sort_ls[-1]] != 0:
        marks[sort_ls[-1]] = False
        sort_ls.pop()

    sort_ls.append(ls[i])

[
    print(sort_ls[i], end=' ') 
    if i+1 < len(sort_ls) 
    else print(sort_ls[i]) 
    for i in range(k)
]


