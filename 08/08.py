### Both parts ###
import numpy as np
import re

with open('08.in') as input:
	lines = input.readlines()
arr = np.zeros((6,50))
for line in lines:
	cmd = re.split('[ =]',line.rstrip())
	if cmd[0] == 'rect':
		x,y = cmd[1].split('x')
		for i in range(int(x)):
			for j in range(int(y)):
				arr[j,i] = 1
	if cmd[0] == 'rotate':
		rk = int(cmd[3])
		shift = int(cmd[5])
		if cmd[1] == 'column':
			arr.T[rk] = np.roll(arr.T[rk], shift)
		else:
			arr[rk] = np.roll(arr[rk], shift)
print np.sum(arr)
print "\n".join(''.join('#' if x else ' ' for x in row) for row in arr)

