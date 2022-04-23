ten9 = 10**9
def pots(ini, fin):
    x = []
    for i in range(ini, fin+1):
        x.append(ten9-i)
    return x

two29 = 1<<29;
twos = {}
twos[30] = [two29-1, two29+1]
twos[31] = pots(0, 1) + [147483649]
twos[32] = pots(2, 5) + [294967310]
twos[33] = pots(6, 13) + [589934668]
twos[34] = pots(14, 30) + [179869558]
twos[35] = pots(31, 64) + [359739983]

def genA():
    A = []
    for i in range(30):
        A.append(1<<i)
    delta = 1
    for i in range(30, 35):
        A.extend(twos[i])
    x = 1025
    while (len(A)<100):
        A.append(x)
        x+=1
    A.sort()
    return A

def ver(e):
    if e < 30:
        return [1<<e]
    return twos[e]
    

A = genA()
As = [str(x) for x in A]
T = int(input())
for caso in range(1, T+1):
    N = int(input())
    print(' '.join(As))
    B = [int(x) for x in input().split()]
    S = sum(A) + sum(B)
    S = S//2
    sol = []
    LIM = (1<<35)-1
    B.sort()
    while (S > LIM and len(B)>0):
        b = B.pop()
        sol.append(b)
        S -= b   
    L = list(bin(S)[2:])
    L.reverse()
    L = [int(x) for x in L]
    for i in range(len(L)):
        if L[i]==1:
            sol.extend(ver(i))
    sol.sort()
    sol = [str(x) for x in sol]
    print(' '.join(sol))
    

            
    

    
    


    
    
    
