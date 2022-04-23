import sys
import math

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return list(map(int, input().split()))

def count_letter(str_, letter):
    
    count = 0
    
    for char_ in str_:
        if char_ == letter:
            count += 1

    return count


N = read()

word = input()

print(f"{count_letter(word, 'a')} {count_letter(word, 'z')}")