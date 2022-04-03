import sys

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())


num_employees, raise_ = read_line()
double_choice = 0
raise_choice = 0

for i in range(num_employees):
    salary = read()

    if salary > raise_:
        double_choice += 1
    elif raise_ > salary:
        raise_choice += 1

# print(raise_choice)
# print(double_choice)

if double_choice == raise_choice:
    print(0)
else:
    print(1 if raise_choice > double_choice else 2)

