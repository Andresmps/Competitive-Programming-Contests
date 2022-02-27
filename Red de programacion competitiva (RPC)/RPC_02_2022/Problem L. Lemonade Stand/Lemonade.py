import sys
from math import ceil

input=sys.stdin.readline

def read():
    return int(input().strip())

def read_line():
    return map(int, input().split())


t = read()

for _ in range(t):
	days, lemons_cup, sugar_cup = read_line()

	min_lemon_price, min_sugar_price = 51, 501
	total_lemons, total_sugar = 0, 0
	sugar_onces = 0
	dict_lemon_prices = {}
	dict_sugar_prices = {}

	for _ in range(days):
		cups, price_lemon, price_sugar = read_line()
		min_lemon_price = min(min_lemon_price, price_lemon)
		min_sugar_price = min(min_sugar_price, price_sugar)

		total_lemons += min_lemon_price * lemons_cup * cups

		sugar_onces += (cups * sugar_cup)
		bag_pounds = ceil(sugar_onces / (16*5))

		sugar_onces -= bag_pounds * (16*5)
		total_sugar += bag_pounds * min_sugar_price

	# print(total_lemons)s

	print(total_sugar + total_lemons)
	# print()



