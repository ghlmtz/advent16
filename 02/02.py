### Part one ###
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

### Part two ###
print ""

# I feel lazy so here's all possible combinations
sol = {'1':('1','1','3','1'), '2':('2','2','6','3'), '3':('1','2','7','4'),
       '4':('4','3','8','4'), '5':('5','5','5','6'), '6':('2','5','A','7'),
       '7':('3','6','B','8'), '8':('4','7','C','9'), '9':('9','8','9','9'),
       'A':('6','A','A','B'), 'B':('7','A','D','C'), 'C':('8','B','C','C'),
       'D':('B','D','D','D')}
dir = {'U':0, 'L':1, 'D':2, 'R':3}

# Another recursive function to solve
def r_solve2(line):
	if not line:
		return base
	return sol[r_solve2(line[1:])][dir[line[0]]]

base = '5'

with open('02.in') as input:
	for line in input:
		base = r_solve2(line.rstrip()[::-1])
		print base,
