import re


def is_prime(n):
	if n < 2: return False

	for i in range(2, n):
		if i*i > n: 
			break

		if n % i == 0: 
			return False

	return True


def is_valid_char(x):
	x_num = ord(x)
	if (32 < x_num < 48) or (57 < x_num < 127):
		return False
	return True


def is_valid_ans(str_):
	for x in str_:
		if not is_valid_char(x):
			return False
	return True

str_ = ""

while True:
	try:
		str_ += f"{input()} "
	except EOFError:
		break

str_ = str_.strip()

if is_valid_ans(str_):
	regex_ = r"[\s]+"
	str_clean = re.sub(regex_, " ", str_).strip()
	ls = str_clean.split()

	# print(str_clean)
	# print(ls)

	if len(ls) != 3:
		print(0)
	else:

		if not all([i.isnumeric() and not i.startswith('0') for i in ls]):
			print(0)
		else:
			if (( 3 < int(ls[0]) <= 10**9 ) and (int(ls[0]) % 2 == 0) and
				 is_prime(int(ls[1])) and is_prime(int(ls[2])) and
				 int(ls[1]) + int(ls[2]) == int(ls[0])):
			 	print(1)
			else:
				print(0)
else:
	print(0)
# print(ls)

# print([[i, chr(i)] for i in range(32, 127)])
