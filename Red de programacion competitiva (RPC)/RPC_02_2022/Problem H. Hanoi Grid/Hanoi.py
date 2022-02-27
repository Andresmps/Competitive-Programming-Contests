import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())


for i in range(read()):
    number_disks, matrix_size = read_line()
    max_number_disks = (matrix_size-1) * (matrix_size-1)

    if number_disks - 1 > max_number_disks:
        print(f"Grid #{i+1}: impossible")
    else:
        print(f"Grid #{i+1}: {2*number_disks*(matrix_size-1)}")

    print()