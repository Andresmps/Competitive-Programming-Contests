
sum_beta = 0

for i in range(1011):
	print(1012+i, ' ', 2022-i)
	sum_beta += 1/ ((1012+i)*(2022-i))
	print(1/ ((1012+i)*(2022-i)))




sum_alpha = 0

for i in range(1, 1012):
	print(2*i - 1, ' ', 2*i)
	sum_alpha += 1/ (((2*i)-1)*(2*i))
	print(1/ (((2*i)-1)*(2*i)))

print()
print(sum_alpha)
print(sum_beta)

alpha = 2021 / 2022
beta = 0.00045675673156653093

print()
print(alpha)

print( round(alpha / beta, 6) )

print( round(sum_alpha / sum_beta, 6) )