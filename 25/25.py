def reg(l):
	return ord(l)-97
def oreg(l):
	try:
		return int(l)
	except:
		return regs[ord(l)-97]
with open('25.in') as input:
	lines = input.readlines()
tgl_tbl = {'cpy': 'jnz', 'inc': 'dec', 'dec': 'inc',
           'jnz': 'cpy', 'tgl': 'inc', 'out': 'inc'}
# Slurp up the commands into our big command list thing
cmds = [c.split() for c in lines]
regs = [0,0,0,0]

def try_input():
	cs = 0
	out = 1
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
				continue
		elif cmds[cs][0] == 'tgl':
			t = oreg(vars[0])
			if cs + t < len(cmds):
				cmds[cs + t][0] = tgl_tbl[cmds[cs + t][0]]
		elif cmds[cs][0] == 'out':
			if out == 1 and oreg(vars[0]) == 0:
				out = 0
			elif out == 0 and oreg(vars[0]) == 1:
				out = 1
			else:
				return
		cs += 1

a = 0
while True:
	print a
	regs[0] = a
	try_input()
	# Answer is the one it hangs on
	a += 1
