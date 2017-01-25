import re

def r_solve(line):
	if len(line) == 1:
		return 2
	result = r_solve(line[1:])
	if(line[0] == 'D' or line[0] == 'R'):
		return 2 if result == 1 else 3
	else:
		return 2 if result == 3 else 1

with open('02.in') as input:
	for line in input:
		y = r_solve(re.sub('L|R','',line.rstrip()[::-1]))
		x = r_solve(re.sub('U|D','',line.rstrip()[::-1]))
		print(x + 3*(y-1)),
