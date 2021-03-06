### Part one ###
import re

ids = 0
with open('04.in') as input:
	for line in input:
		name = "".join(re.match('(.*)-\d',line).group(1).split('-'))
		set_name = set(name)
		s_name = sorted(set_name,key=lambda x:-500*name.count(x)+ord(x))
		chksum = re.search('\[(.*)]',line).group(1)
		if chksum == "".join(s_name[:5]):
			ids += int(re.search('\d+',line).group(0))
print ids

### Part two ###
import string

s = "abcdefghijklmnopqrstuvwxyz"
with open('04.in') as input:
	for line in input:
		names = re.split('-',line)
		rot = int(re.search('\d+',line).group(0)) % 26
		table = string.maketrans(s,s[rot:]+s[:rot])
		for name in names:
			if name.translate(table).startswith('north'):
				print int(re.search('\d+',line).group(0))
