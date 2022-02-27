import re

main_str_ = input()
t = int(input())

for _ in range(t):

	str_, val = input().split()
	# print(str_, val)

	val = int(val)
	regex = fr"({str_}){{1}}"
	
	matches = re.finditer(regex, main_str_)
	matches_ = list(matches)

	if val > len(matches_):
		print(-1)
		continue

	match = matches_[val - 1]
	print(match.start() + 1)
