n = int(input())
weights = [int(input()) for _ in range(n)]
ts = []

sort_weights = sorted(weights)
pref_sum, suf_sum = [0], [0]
sum_1, sum_2 = 0, 0

for i in range(len(sort_weights)):
	ts.append(sort_weights[i])

	if i+1 < len(sort_weights) and sort_weights[i+1] - sort_weights[i] > 1:
		ts.append(sort_weights[i] + 1)


print(f"ls: {sort_weights}")
# print(ts)


for i in range(len(sort_weights)):

	sum_1 += sort_weights[i]
	sum_2 += sort_weights[len(sort_weights) - i - 1]

	pref_sum.append(sum_1)
	suf_sum.append(sum_2)


indices = []
unique_ = sorted(set(sort_weights))
k = 0

for i in range(len(sort_weights)):
	if k >= len(unique_):
		break
	# print(k)
	# print(indices)
	if sort_weights[i] == unique_[k]:
		indices.append(i)
		k+=1

print(f"ind: {indices}")

suf_sum = [0] + suf_sum[::-1] 
pref_sum = pref_sum + [0]
i = 0

for t in ts:
	if i >= len(sort_weights):
		break

	# print(f"t: {t}, i: {i}, ls[i]: {sort_weights[i]}")

	if t == sort_weights[indices[i]]:
		j = indices[i]
		
		# print(f"j: {j}")
		# print(f"{pref_sum[i]} == {suf_sum[j+2]}")

		if pref_sum[indices[i]] == suf_sum[j+2]:	
			print(t)
			break

		i = j+1

	elif t < sort_weights[indices[i]]:

		# print(f"{pref_sum[i]} == {suf_sum[i+1]}")

		if pref_sum[indices[i]] == suf_sum[indices[i]+1]:
			print(t)
			break

# 	print()

# print(pref_sum)
# print(suf_sum)