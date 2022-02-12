
array_bool = [0 for i in range(86401)]


def get_seconds(h, m, s):
	return h*60*60 + m*60 + s


def count_start_jobs(x, type_):

	if x == '*':
		return 24 if type_ == 'h' else 60

	counts_jobs = 0
	x_vals = x.split(',')

	for val in x_vals:
		if '-' not in val:
			counts_jobs += 1
			continue

		a, b = [int(k) for k in val.split('-')]
		counts_jobs += b - a + 1

	return counts_jobs


def get_range_time(x, type_):

	if x == '*':
		return [i for i in range(24 if type_ == 'h' else 60)] 

	counts_jobs = 0
	x_vals = x.split(',')
	temp_ls = []

	for val in x_vals:
		if '-' not in val:
			temp_ls.append(int(val))
			continue

		a, b = [int(k) for k in val.split('-')]

		for k in range(a, b+1):
			temp_ls.append(k)

	return temp_ls


def count_non_repeated_start_jobs(h, m, s):

	hours = get_range_time(h, 'h')
	minutes = get_range_time(m, 'm')
	seconds = get_range_time(s, 's')

	# print(hours)
	# print(minutes)
	# print(seconds)

	for h_ in hours:
		for m_ in minutes:
			for s_ in seconds:
				seconds_ = get_seconds(h_, m_, s_)
				array_bool[seconds_] = 1
		

n = int(input())
ls = [input() for i in range(n)]
total_jobs_runs = 0

for i in range(n):
	h, m, s = ls[i].split()

	# print(ls[i])
	# print(h, '-', m, '-', s)
	
	total_jobs_runs += (
		count_start_jobs(h, 'h') *
		count_start_jobs(m, 'm') *
		count_start_jobs(s, 's')
	)

	count_non_repeated_start_jobs(h, m, s)
	# print(total_jobs_runs)
	# print()

# print([(i, array_bool[i]) for i in range(len(array_bool))])

total_non_repeated_jobs_runs = sum(array_bool)

print(f"{total_non_repeated_jobs_runs} {total_jobs_runs}")