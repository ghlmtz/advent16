from collections import defaultdict, deque
import itertools as it

# 1) get map and make it readable to our program
with open('24.in') as input:
	lines = input.readlines()
h = sum(1 for line in lines)
w = sum(1 for c in lines[0].strip())
maze = [[False for x in range(w)] for y in range(h)]
points = {}

for y,line in enumerate(lines):
	for x,c in enumerate(line.strip()):
		if c != '#':
			maze[y][x] = True
			if c != '.':
				points[c] = (x,y)
# 2) calculate costs for point-to-point paths (should be 28 of them)
costs = [[0 for x in range(len(points))] for y in range(len(points))]

def is_space(pos):
	x = pos[0]
	y = pos[1]
	return maze[y][x]
def p_hash(pos):
	return "%d.%d"%(pos[0],pos[1])
def s_to_d(pos):
	return [int(i) for i in pos.split('.')]
def dist(pos1,pos2):
	return abs(sum(pos2)-sum(pos1))

for tup in it.combinations(points.keys(), 2):
	start = points[tup[0]]
	goal = points[tup[1]]
	queue = deque()
	moves = set()
	prev = {}
	queue.append(p_hash(start))
	moves.add(p_hash(start))

	while queue:
		curr = queue.popleft()
		l_curr = s_to_d(curr)
		if curr == p_hash(goal):
			break

		for dx in [-1,0,1]:
		  for dy in [-1,0,1]:
		    if dx == 0 and dy != 0 or dy == 0 and dx != 0:
			l_neighbor = [sum(c) for c in zip(l_curr, [dx, dy])]
			neighbor = p_hash(l_neighbor)
			if neighbor in moves:
				continue
			if not is_space(l_neighbor):
				continue
			elif neighbor not in queue:
				queue.append(neighbor)
				moves.add(neighbor)
			prev[neighbor] = curr

	path = [curr]
	while curr in prev.keys():
		curr = prev[curr]
		path.append(curr)

	costs[int(tup[0])][int(tup[1])] = costs[int(tup[1])][int(tup[0])] = len(path)-1

# 3) run through all possible paths and find lowest cost (should be 7! of them)
zero = points.pop('0')
min_cost = 10000
for perm in it.permutations(points):
	sum = costs[0][int(perm[0])]
	for N,p in enumerate(perm):
		if N+1 == len(perm):
			break
		sum += costs[int(p)][int(perm[N+1])]

	# Following line is for part 2
	sum += costs[0][int(perm[-1])]

	if sum < min_cost:
		min_cost = sum
# 4) congrats
print min_cost
