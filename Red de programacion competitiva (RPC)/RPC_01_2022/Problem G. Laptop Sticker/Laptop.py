wc, hc, ws, hs = [int(i) for i in input().strip().split()]

if (wc - ws >= 2) and (hc - hs >= 2):
	print("1")
else:
	print("0")
