import hashlib,re
import binascii

input = 'ngcjuoqr'
#input = 'abc'
i = 0
n = 0
check = {}
good = {}
accept = 1
while accept:
	if accept > 1 and i > accept:
		break
	m = hashlib.md5()
	m.update(input + str(i))
	hex_str = binascii.hexlify(m.digest())
	for five in check.keys():
		if check[five][1] < i:
			del check[five]
			continue
		if hex_str.count(check[five][0]):
			good[check[five][1]-1000] = five
			del check[five]
			n += 1
			if n > 64:
				accept = i + 1000
	match = re.search(r'(.)\1\1',hex_str)
	if match:
		check[hex_str] = [(match.group(0)+match.group(0))[:5], i + 1000]
	i += 1
print sorted(good.keys())[63]
