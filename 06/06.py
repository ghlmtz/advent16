### Both parts! ###
with open('06.in') as input:
	lines = input.readlines()
one = ''
two = ''
for i in range(len(lines[0])):
	col = ''
	for line in lines:
		col += line[i]
	one += sorted(col,key=lambda x:col.count(x))[-1]
	two += sorted(col,key=lambda x:col.count(x))[0]
print one,
print two,
