with open('15.in') as input:
	lines = input.readlines()
discs = []
val_init = []
for N,line in enumerate(lines):
	discs.append(int(line.split()[3]) )
	val_init.append((int(line.split()[11][:-1])+N+1) % int(line.split()[3]))
	print N
#For Part Two, new 11 disc
discs.append(11)
val_init.append(0+len(val_init)+1)
# Use Chinese Remainder Theorem from number theory to help us out
m = reduce(lambda x, y: x * y, discs)
for i in range(m):
	result = 1
	for n in range(len(val_init)):
		if (val_init[n] + i) % discs[n] != 0:
			result = 0
	if result:
		break
print i
