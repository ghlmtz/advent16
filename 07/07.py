### Part one ###
import re

def abba(s):
	return ( s[0] == s[3] and s[1] == s[2] and s[0] != s[1] )

with open('07.in') as input:
	lines = input.readlines()
count = 0
for N,addr in enumerate(lines):
	blk = 0
	yes = 0
	for i in range(len(addr)-4):
		substr = addr[i:i+4]
		if blk == 1:
			if substr.count('['):
				continue
			blk = 2
		if blk == 2:
			if substr.count(']'):
				blk = 3
				continue
			if(abba(substr)):
				yes = 0
				break
		if blk == 3:
			if substr.count(']'):
				continue
			blk = 0
		if blk == 0:
			if substr.count('['):
				blk = 1
				continue
			if(abba(substr)):
				yes = 1
	if yes == 1:
		count += 1
print count
