import re

moves = [1,1,2,2,3,3]

def r_solve(line):
	if len(line) == 1:
		return 2
	result = r_solve(line[1:])
	if(line[0] == 'D' or line[0] == 'R'):
		return moves[result+2]
	else:
		return moves[result-1]

with open('02.in') as input:
	for line in input:
		print re.sub('L|U','',line)
