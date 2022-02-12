MAX = 10**6

prime_bool = [True for i in range(MAX+1)]
primes = [2]


def is_prime(n):
	if n < 2: return False

	for i in range(2, n):
		if i*i > n: break
		if n % i == 0: return False

	return True


def sieve():
	for i in range(4, MAX, 2):
		prime_bool[i] = False

	for i in range(3, MAX, 2):
		if i*i >= MAX:
			break 

		if not prime_bool[i]:
			continue

		primes.append(i)

		for j in range(i*i, MAX, i):
			prime_bool[j] = False

	for i in range(3, MAX, 2):
		if not prime_bool[i]:
			continue
		primes.append(i)

sieve()
print(primes[:100])
# print(prime_bool)