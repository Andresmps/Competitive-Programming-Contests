n = int(input())

# Solve equation x / y = n, where:
# - n is Integer.
# - x and y contains just five digits from 0 to 9 without repetition.

while True:

	if n == 0:
		break

	# From the equation y in [ceil(1234/y), ceil(98765/y)] ->
	# (By problem requirements) [1234, ceil(98765/y)]
	upper_limit = (98765 // n) + 1
	flag = False

	for y in range(1234, upper_limit):
		
		# Define a set with all digits of x and y and look
		# if it contains numbers from 0 to 9
		temp_set = set()
		temp_set.update(str(y).zfill(5), str(y*n))
		
		if len(temp_set) == 10:
			print(f"{y*n} / {str(y).zfill(5)} = {n}")
			flag = True

	if not flag:
		print(f"There are no solutions for {n}.")

	n = int(input())
	if n != 0: print()
