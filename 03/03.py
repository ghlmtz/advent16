### Part one ###
count = 0
with open('03.in') as input:
	for line in input:
		nums = [int(c) for c in line.split()]
		if max(nums) < sum(nums)/2.0:
			count += 1
print count

### Part two ###
count = 0
with open('03.in') as input:
	lines = input.readlines()
for x in range(len(lines)/3):
	for i in range(3):
		nums = [int(lines[3*x].split()[i]), int(lines[3*x+1].split()[i]), int(lines[3*x+2].split()[i])]
		if max(nums) < sum(nums)/2.0:
			count += 1
print count
