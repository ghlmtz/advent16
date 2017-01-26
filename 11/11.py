import re
import itertools
import collections

items = []
moves = set()
times = collections.defaultdict(set)
# Build our array of items
with open('11.in') as input:
	lines = input.readlines()
for line in lines:
	gen = set(name[:2]+"G" for name in re.findall('(\w+) generator',line))
	chip =set(name[:2]+"M" for name in  re.findall('(\w+)-compatible',line))
	items.append(gen | chip)
items[0].add('EEE') # Don't forget the elevator!
# Below are for part two, comment them out to get part one answer
items[0].add('elG')
items[0].add('elM')
items[0].add('diG')
items[0].add('diM')
#This is a fun hash function
def flr_hash(i):
	ret = ""
	for flr in i:
		f_ret = [0,0,0]
		for item in flr:
			if item[:2]+'G' in flr and item[:2]+'M' in flr:
				f_ret[0] += 1
			elif item[-1] == 'G':
				f_ret[1] += 1
			elif item[-1] == 'M':
				f_ret[2] += 1
		if 'EEE' in flr:
			ret += 'E'
		ret += "".join(str(f_ret))
	return ret
#This function will give us a string representation of our current status
def flr_str(i):
	ret = "1"+"".join(sorted(i[0]))
	ret += "2" + "".join(sorted(i[1]))
	ret += "3" + "".join(sorted(i[2]))
	ret += "4" + "".join(sorted(i[3]))
	return ret
#This function turns a flr_str back into a set
def flr_set(s):
	flrs = re.split('\d',s)[1:]
	ret = []
	for N,flr in enumerate(flrs):
		ret.append(set())
		for i in xrange(0, len(flr), 3):
			ret[N].add(flr[i:i+3])
	return ret
def chk(i):
	for floor in i:
		for item in floor:
			if item.count('M') and item[:2]+"G" not in floor and "G" in "".join(floor):
				return 1000
	return 1
def debug(f):
	s = re.split('\d',f)[::-1]
	return re.sub('([A-Z])','\g<1> ',"\n".join(s[:-1]))
moves.add(flr_hash(items))
times[0].add(flr_str(items))
ans = 0
for time in range(100):
#  print "Level",time,"Size",len(moves)
  for mstr in times[time]:
	if mstr.startswith('1234'):
		ans = time
		break
	items = flr_set(mstr)
	n_items = flr_set(mstr)
	for N,f_items in enumerate(items):
		if 'EEE' in f_items:
			n_items[N].remove('EEE')
			for item in f_items:
				if item == 'EEE':
					continue
				for flr in range(4):
					if flr != N-1 and flr != N+1:
						continue
					n_items[N].remove(item)
					n_items[flr].add('EEE')
					n_items[flr].add(item)
					our_str = flr_str(n_items)
					our_hash = flr_hash(n_items)
					if our_hash not in moves:
						moves.add(our_hash)
						idx = time+chk(n_items)
						if idx < 1000:
							times[idx].add(our_str)
					n_items[flr].remove('EEE')
					n_items[flr].remove(item)
					n_items[N].add(item)
			for item1,item2 in itertools.combinations(f_items,2):
				if item1 == 'EEE' or item2 == 'EEE':
					continue
				for flr in range(4):
					if flr != N+1:
						continue
					n_items[N].remove(item1)
					n_items[N].remove(item2)
					n_items[flr].add('EEE')
					n_items[flr].add(item1)
					n_items[flr].add(item2)
					our_str = flr_str(n_items)
					our_hash = flr_hash(n_items)
					if our_hash not in moves:
						moves.add(our_hash)
						idx = time+chk(n_items)
						if idx < 1000:
							times[idx].add(our_str)
					n_items[flr].remove('EEE')
					n_items[flr].remove(item1)
					n_items[flr].remove(item2)
					n_items[N].add(item1)
					n_items[N].add(item2)
	if ans > 0:
		break
  if ans > 0:
	break
print ans
#print moves
#print times
