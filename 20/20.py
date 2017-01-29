with open('20.in') as input:
	lines = input.readlines()
black = []
for line in lines:
	a,b = [int(i) for i in line.strip().split('-')]
	black.append((a,b))
black = sorted(black)

i = 0
ip = 0
while i < 2**32:
	for l,h in black:
		if i >= l and i <= h:
			# Skip past this section since it's all blocked
			i = h
			break
	else:
		if ip == 0:
			print i # Part one
		ip += 1
	i += 1
print ip # Part two
