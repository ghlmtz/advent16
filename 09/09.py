### Part one ###
import re

with open('09.in') as input:
	line = input.read()
mk = 0
out = ""
while mk < len(line):
	ch = line[mk]
	if ch == '(':
		s_idx = mk
		while line[mk] != ')':
			mk += 1
		mk += 1
		n,xx = re.match('\((\d+)x(\d+)\)',line[s_idx:mk]).groups()
		s_idx = mk
		mk += int(n)
		for _ in range(int(xx)):
			out += line[s_idx:mk]
	else:
		out += ch
		mk += 1
print len(out.rstrip())
