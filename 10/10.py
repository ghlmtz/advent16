### Definitely not pretty ###

import re

with open('10.in') as input:
	lines = input.readlines()
bots = {}
output = {}
class Bot:
	v1 = 0
	v2 = 0
	low = None
	high = None
	output = 0
	def setlh(self,low,high):
		self.low = low
		self.high = high
	def act(self):
		if(self.v1 != 0 and self.v2 !=0):
			if self.output % 2 == 1:
				output[self.low] = min(self.v1,self.v2)
			else:
				bots[self.low].setv(min(self.v1,self.v2))
			if self.output > 1:
				output[self.high] = max(self.v1,self.v2)
			else:
				bots[self.high].setv(max(self.v1,self.v2))
			self.v1 = 0
			self.v2 = 0
	def setv(self,x):
		if self.v2 > 0 and self.v1 > 0:
			return
		if self.v1 == 0:
			self.v1 = x
		elif self.v2 == 0:
			self.v2 = x
	def debug(self):
		print self.v1,self.v2,self.low,self.high

ans = 0
mul = 0
while mul == 0:
	for line in lines:
		col = line.split()
		if line.startswith('v'):
			if col[5] not in bots:
				bots[col[5]] = Bot()
			bots[col[5]].setv(int(col[1]))
		else:
			if col[1] not in bots:
				bots[col[1]] = Bot()
			bots[col[1]].setlh(col[6],col[11])
			bots[col[1]].output = 0
			if col[5] == 'output':
				bots[col[1]].output += 1
			if col[10] == 'output':
				bots[col[1]].output += 2
			if bots[col[1]].v1 == 17 and bots[col[1]].v2 == 61:
				ans = col[1]
			bots[col[1]].act()
	if '0' in output and '1' in output and '2' in output:
		mul = output['0'] * output['1'] * output['2']
print ans
print mul
