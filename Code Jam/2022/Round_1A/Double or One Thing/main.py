import sys
# import random

# RANDOM_SEED = 42
# MIN_AB = 1
# MAX_AB = 10**9 + 10


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



T = int(input())

for t_ in range(T):
  N = int(input())

  # choices = [i for i in range(1, 500)]
  # A = []

  # for i in range(N):
  #   temp_ = i*20 % 500
  #   if temp_ not in A:
  #     A.append(choices.pop(temp_))

  # A = list(map(int, input().split()))

  # random.seed(RANDOM_SEED + t_)
  # A = list(random.sample(range(MIN_AB, MAX_AB), N))
  
  # A = genA()[:N]

  A = [(i*3) % (10 ** 9) for i in range(1, N+1)]

  A_ = [str(s) for s in A]
  print(" ".join(A_))
  sys.stdout.flush()

  B = list(map(int, input().split()))
  A.extend(B)
  A = sorted(A)[::-1]
  mid_sum = sum(A)//2
  solution = []
  flag = False

  for i in range(len(A)):
    temp_sum = A[i]
    solution.append(A[i])
    for j in range(len(A)):
      if i == j:
        continue

      if temp_sum + A[j] > mid_sum:
        continue
      elif temp_sum + A[j] < mid_sum:
        temp_sum += A[j]
        solution.append(A[j])
      else:
        flag = True
        solution.append(A[j])
        break

    if flag:
      break

  [print(i, end=' ') for i in solution[:-1]]
  print(solution[-1])
  sys.stdout.flush()









