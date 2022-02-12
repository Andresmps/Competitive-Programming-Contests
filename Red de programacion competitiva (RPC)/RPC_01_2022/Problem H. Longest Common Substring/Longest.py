n = int(input().strip())
ls = []


def sub_str_in_str(main_str, array_strs):
	for str_ in array_strs:
		if main_str not in str_:
			return False
	return True


for i in range(n):
	ls.append(input().strip())

max_sub_str = 0
start, end = 0, 1

while end <= len(ls[0]):

	# print(start, '-', end)
	# print(ls[0][start:end])

	if sub_str_in_str(ls[0][start:end], ls[1:]):
		
		# print(True)
		max_sub_str = max(max_sub_str, len(ls[0][start:end]))
		end += 1
	else:
		# print(False)
		start += 1
		end = start + 1

	# print(max_sub_str)
	# print()


# print('---')
print(max_sub_str)

