regs = [0,0,0,0]
#part two
regs[2] = 1
cs = 0
def reg(l):
	return ord(l)-97
def oreg(l):
	try:
		return int(l)
	except:
		return regs[ord(l)-97]
with open('12.in') as input:
	lines = input.readlines()
while cs < len(lines):
	cmd = lines[cs].split()
	if cmd[0] == 'cpy':
		regs[reg(cmd[2])] = oreg(cmd[1])
	elif cmd[0] == 'inc':
		regs[reg(cmd[1])] += 1
	elif cmd[0] == 'dec':
		regs[reg(cmd[1])] -= 1
	elif cmd[0] == 'jnz':
		if oreg(cmd[1]) != 0:
			cs += oreg(cmd[2])
#			print "JUMPING",oreg(cmd[2])
			continue
	cs += 1
print "a =",regs[0]
