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

### Part two ###
i = 0
password = '________'
while password.count('_'):
	m = hashlib.md5()
	m.update(input + str(i))
	hex_str = binascii.hexlify(m.digest())
	if hex_str.startswith('00000') and int(hex_str[5],16) < 8:
		idx = int(hex_str[5])
		if password[idx] == '_':
			password = password[:idx] + hex_str[6] + password[idx+1:]
	i += 1
print password
