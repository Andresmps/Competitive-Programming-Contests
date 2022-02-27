import sys

input=sys.stdin.readline
def IN():
    return int(input().strip())
def INL():
    return map(int,input().split())

"""
**************
INICIO
**************
"""

def calculo():
    mid_pesos=sum(l)//2
    peso=0
    i=0
    while i <  len(l):
        peso+=l[i]

        if peso > mid_pesos:
            print(l[i])
            break

        if peso == mid_pesos:
            if l[i] == l[i+1]:
                print(l[i])
            else:
                print(l[i]+1)
            break
        i+=1

l=[]
for _ in range(IN()):
    l.append(IN())
l.sort()
#print(l)

calculo()
