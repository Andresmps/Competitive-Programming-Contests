a, b = [int(i) for i in input().split()]

count = 0

if a < b:
	print(b-a)
else:

	while a > b:
		count += 1
		if a % 2 != 0 or a < b:
			a += 1

		else:
			a /= 2

	if a < b:
		print(int(b - a) + count)
	else:
		print(count)