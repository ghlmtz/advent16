regs = [7,0,0,0]
cs = 0
def reg(l):
	return ord(l)-97
def oreg(l):
	try:
		return int(l)
	except:
		return regs[ord(l)-97]
with open('23.in') as input:
	lines = input.readlines()
tgl_tbl = {'cpy': 'jnz', 'inc': 'dec', 'dec': 'inc',
           'jnz': 'cpy', 'tgl': 'inc'}
# Slurp up the commands into our big command list thing
cmds = [c.split() for c in lines]
while cs < len(cmds):
	vars = cmds[cs][1:]
	if cmds[cs][0] == 'cpy':
		if not vars[1].isalpha():
			print "Not alpha"
		regs[reg(vars[1])] = oreg(vars[0])
	elif cmds[cs][0] == 'inc':
		regs[reg(vars[0])] += 1
	elif cmds[cs][0] == 'dec':
		regs[reg(vars[0])] -= 1
	elif cmds[cs][0] == 'jnz':
		if oreg(vars[0]) != 0:
			cs += oreg(vars[1])
#			print "JUMPING",oreg(vars[1])
			continue
	elif cmds[cs][0] == 'tgl':
		t = oreg(vars[0])
		if cs + t < len(cmds):
			cmds[cs + t][0] = tgl_tbl[cmds[cs + t][0]]
	cs += 1
print "a =",regs[0]

# Based on trial and error I figured out how the second part works
# a! + CONSTANT determined in the code
