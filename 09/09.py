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

### Part two ###
def process(s):
	if '(' not in s:
		return len(s)
	sum = 0
	while '(' in s:
		s_idx = s.find('(')
		e_idx = s.find(')')+1
		sum += s_idx
		n,xx = re.match('\((\d+)x(\d+)\)',s[s_idx:]).groups()
		next = s[e_idx:e_idx+int(n)]
		sum += int(xx)*process(next)
		s = s[e_idx+int(n):]
	return sum

print process(line.rstrip())
