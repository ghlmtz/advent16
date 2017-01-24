### Part One ###
with open('01.in') as input:
	line = input.read().rstrip().split(', ')
# Convert our Ls and Rs to machine readable tuples
rel_dirs = [((-1,1)[(x[0] == 'R')],int(x[1:])) for x in line]
# Sum through all the directions
D = 0
sums = [0,0,0,0]
for dir in rel_dirs:
	D = (D + dir[0]) % 4
	sums[D] += dir[1]
# Print our taxicab distance
print abs(sums[0]-sums[2]) + abs(sums[1]-sums[3])
