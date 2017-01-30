from itertools import permutations

with open('21.in') as input:
	lines = input.readlines()

password = "abcdefgh"
password2 = "fbgdceah"

def solve(pwd):
	l_pwd = list(pwd)
	for cmd in lines:
		words = cmd.split()
		if words[0] == 'swap':
			if words[1] == 'position':
				a, b = int(words[2]), int(words[5])
			if words[1] == 'letter':
				a, b = l_pwd.index(words[2]), l_pwd.index(words[5])
			l_pwd[a], l_pwd[b] = l_pwd[b], l_pwd[a]
		if words[0] == 'reverse':
			a, b = int(words[2]), int(words[4])
			l_pwd = l_pwd[0:a] + list(reversed(l_pwd[a:b+1])) + l_pwd[b+1:]
		if words[0] == 'move':
			a, b = int(words[2]), int(words[5])
			l = l_pwd[a]
			l_pwd.remove(l)
			l_pwd.insert(b, l)
		if words[0] == 'rotate':
			if words[1] == 'based':
				a = l_pwd.index(words[6])
				a += 2 if a >= 4 else 1
				a = a % len(l_pwd)
				a = len(l_pwd) - a
			else:
				a = int(words[2])
				if words[1] == 'right':
					a = len(l_pwd) - a
			l_pwd = l_pwd[a:] + l_pwd[0:a]
	return "".join(l_pwd)

print solve(password)

for p in permutations(password):
	if solve(p) == password2:
		print "".join(p)
		break
