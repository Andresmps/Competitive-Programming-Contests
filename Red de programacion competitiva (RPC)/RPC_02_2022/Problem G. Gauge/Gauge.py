import math

PI = 3.14159265358979


def area_arc(k, r, l, x):
	area = (
		(k**2/2) +
		((1/2) * k * math.sqrt(r**2-k**2)) - ((l+x)*k) +
		((r**2/2) * math.asin(k/r))
	)

	return area


def get_intercept(r, l):
	x = math.sqrt(r**2 - l**2) if l <= r else -1

	return x


def area_cir(r):
	return PI * r**2


n = int(input())

for _ in range(n):
	lon, r = [int(i) for i in input().split()]

	# Focus on one plane quadram

	lon_ = lon / 2
	x = get_intercept(r, lon_)
	# print(lon_, r, x)

	if lon_ >= r:
		# print("I")
		res = area_cir(r) / 4
	elif x >= lon_:
		# print("II")
		res = lon_**2
	else:
		# print("III")
		res = (
			lon_**2 - ((lon_-x)**2 / 2) + area_arc(lon_, r, lon_, x) - area_arc(x, r, lon_, x)
		)

	res *= 4
	res = round(res, 2)
	print("{:.2f}".format(res))
	# print()


# print(area_arc(4) - area_arc(3))
# print(get_intercept(5, 8))