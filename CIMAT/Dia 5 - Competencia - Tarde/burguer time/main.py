import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

T = read()

while T != 0:

    roadway = input().strip()
    min_dis = 2000001
    last_place = -1
    # print(roadway)

    for i in range(len(roadway)):

        place = roadway[i]
        # print(place)
        # print(min_dis)
        # print(last_place)

        if place == 'Z':
            min_dis = 0
            break

        if place == '.':
            continue

        if last_place == -1:
            last_place = i

        if roadway[last_place] == place:
            last_place = i
        else:
            min_dis = min(min_dis, i-last_place)
            last_place = i


    print(min_dis)
    # print()
    
    T = read()


