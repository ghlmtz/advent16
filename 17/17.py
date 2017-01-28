from collections import deque
from itertools import compress
from hashlib import md5

def is_open(path):
	return [int(x, 16) > 10 for x in md5(path).hexdigest()[:4]]

def path2loc(path):
	return [path.count('D') - path.count('U'), path.count('R') - path.count('L')]

input = 'vkjiggvb'
loc = [1,1]
queue = deque()
for i in compress('UDLR',is_open(input)):
	queue.append(i)
longest = 0
shortest = None
while queue:
	curr = queue.popleft()
	loc = path2loc(input + curr)
	if loc == [3, 3]:
		if not shortest:
			shortest = curr
		longest = len(curr)
		continue
	for i in compress('UDLR',is_open(input + curr)):
		nloc = path2loc(curr + i)
		if nloc[0] < 0 or nloc[0] > 3 or nloc[1] < 0 or nloc[1] > 3:
			continue
		queue.append(curr + i)
print shortest
print longest
