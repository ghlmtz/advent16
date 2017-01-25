### Part one ###
count = 0

with open('03.in') as input:
	for line in input:
		nums = [int(c) for c in line.split()]
		if max(nums) < sum(nums)/2.0:
			count += 1
print count
