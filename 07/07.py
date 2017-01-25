### Part one ###
import re

def abba(s):
	if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
		return True
	else:
		return False

with open('07.in') as input:
	lines = input.readlines()
for addr in lines:
	

