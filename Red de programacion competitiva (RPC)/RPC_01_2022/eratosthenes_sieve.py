MAX = 5*10**6

prime_bool = [True for i in range(MAX+1)]
primes = [2]


def is_prime(n):
	if n < 2: return False

	for i in range(2, n): # O(sqrt(n))
		if i*i > n: break
		if n % i == 0: return False

	return True


def sieve(): # O( sqrt(MAX)  * log(MAX) )

	for i in range(4, MAX, 2): # O(MAX / 2)
		prime_bool[i] = False

	for i in range(3, MAX, 2): # O(sqrt(MAX)) * O(log(MAX))
		if i*i >= MAX:
			break 

		if not prime_bool[i]: 
			continue

		primes.append(i)

		for j in range(i*i, MAX, i): # O(log_i(MAX))
			prime_bool[j] = False

	for i in range(3, MAX, 2): # O(MAX / 2)
		if not prime_bool[i]:
			continue
		primes.append(i)

# Llena la lista primes con todos los primos hasta MAX.
# Preferiblemente usar MAX <= 5*10**6 para que no tarde más de un segundo 

sieve()
print(f"primes: {primes[:10]}")

# Además, podemos validar si un número es primo o no
#  con la función is_prime(). Sin embargo, esta función es O(sqrt(n))

print(f"37 is prime? -> {is_prime(37)}")
print(f"25 is prime? -> {is_prime(25)}")
