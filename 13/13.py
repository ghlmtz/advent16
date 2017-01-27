### Part one ###
import collections

input = 1364

def is_space(pos):
	x = pos[0]
	y = pos[1]
	if x < 0 or y < 0:
		return False
	b = bin(x*x + 3*x + 2*x*y + y + y*y + input)
	return not reduce(lambda c,d: int(c)^int(d), b[2:])

def p_hash(pos):
	return "%d.%d"%(pos[0],pos[1])

# Wherein I implement A*
start = [1,1]
goal = [31,39]
queue = set()
moves = set()
prev = {}
queue.add(p_hash(start))
gscore = collections.defaultdict(lambda: 10000)
fscore = collections.defaultdict(lambda: 10000)
gscore[p_hash(start)] = 0
fscore[p_hash(start)] = abs(sum(goal)-sum(start))

def s_to_d(pos):
	return [int(i) for i in pos.split('.')]
def dist(pos1,pos2):
	return abs(sum(pos2)-sum(pos1))

while queue:
	curr = sorted(queue,key=lambda x: dist(goal,s_to_d(x)))[0]
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
		our_gscore = gscore[curr] + dist(l_curr,l_neighbor)
		if not is_space(l_neighbor):
			continue
		elif neighbor not in queue:
			queue.add(neighbor)
		elif our_gscore >= gscore[neighbor]:
			continue
		prev[neighbor] = curr
		gscore[neighbor] = our_gscore
		fscore[neighbor] = gscore[neighbor] + dist(l_neighbor,goal)
	queue.remove(curr)
	moves.add(curr)
path = [curr]
while curr in prev.keys():
	curr = prev[curr]
	path.append(curr)
print len(path)-1

# Here's a cool map of my path
path_set = set(path)
for y in range(50):
	line = ""
	for x in range(50):
		if p_hash([x,y]) in path_set:
			line += "O"
		else:
			if is_space([x,y]):
				line += "."
			else:
				line += "#"
	print line

