### DRAGON CURVE Z ###

input = "10001001100000001"
flip = "".join([['1','0'][int(x)] for x in reversed(input)])
def dragon(n):
	return '1' if ((((n & -n) << 1) & n) != 0) else '0'
n = 1
goal = 35651584
disk = ""
# The whole string is just input and its flip joined together by
# successive digits of the dragon curve
while len(disk) < goal:
	if(n % 2) == 1:
		disk += input
	else:
		disk += flip
	disk += dragon(n)
	n += 1
disk = disk[:goal]
# Given our disk of length <goal>, how long will the checksum string be?
# Checksum will keep dividing length by 2 until length = odd
divisor = 1
while goal % (divisor*2) == 0:
	divisor *= 2
# So checksum will be <goal/divisor> characters long, and for each character
# we need to look at <divisor> chars and evaluate them down to 1 char
# Checksum is a successive XNORing, or an inverse parity bit
while len(disk) > 0:
	slice = disk[:divisor]
	print '1' if reduce(lambda c,d: not(int(c)^int(d)), slice) else '0',
	disk = disk[divisor:]
