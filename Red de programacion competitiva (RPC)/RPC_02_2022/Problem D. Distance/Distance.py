alphabet = input()
query = input()
strings_ = list()


for i in range(len(query)+1):
	for letter in alphabet:
		temp_query = query[:i] + letter + query[i:]
		# print(f"i: {i}")
		# print(temp_query)
		# print(query[:i])
		# print(letter)
		# print(query[i:])
		# print()
		strings_.append(temp_query)

# print(strings_)

for i in range(len(query)):
	temp_query = query[:i] + query[i+1:]
	# print(f"i: {i}")
	# print(temp_query)
	# print(query[:i])
	# print(query[i+1:])
	# print()
	strings_.append(temp_query)

# print(strings_)

for i in range(len(query)):
	for letter in alphabet:
		temp_query = query[:i] + letter + query[i+1:]
		# print(f"i: {i}")
		# print(temp_query)
		# print(query[:i])
		# print(letter)
		# print(query[i+1:])
		# print()
		strings_.append(temp_query)

unique_strings = sorted(set(strings_))
[print(i) for i in unique_strings if i != query]
