### Part one ###
import hashlib, binascii

input = 'wtnhxymk'
i = 0
n = 8
while n > 0:
	m = hashlib.md5()
	m.update(input + str(i))
	hex_str = binascii.hexlify(m.digest())
	if hex_str.startswith('00000'):
		print hex_str[5],
		n -= 1
	i += 1


