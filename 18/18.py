with open('18.in') as input:
	line = input.read().strip()
line = [x == '.' for x in line]
n = line.count(True)
size = 400000	# 40 for part 1
for _ in range(size-1):
	line.insert(0,True)
	line.append(True)
	line = [line[N] == line[N+2] for N,x in enumerate(line[1:-1])]
	n += line.count(True)
print n
