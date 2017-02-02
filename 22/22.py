# I actually solved this one by hand and this helped

with open('22.in') as input:
	lines = input.readlines()

for N,line in enumerate(lines[2:]):
	cols = line.split()
	if int(cols[2][:-1]) < 90:
		if int(cols[2][:-1]) == 0:
			print '_',
		else:
			print '.',
	else:
		print '#',
	if N % 32 == 31:
		print ''
