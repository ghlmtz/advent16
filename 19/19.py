# First part is basically the Josephus problem
# J(2^n) = 1
# J(2^n+k) = 1 + 2*k
def joseph(n):
	div = 1
	while n > div*2:
		div *= 2
	return 2*(n - div) + 1
N = 3012210
print joseph(N)

# Part two is harder
# J(3^n) = 3^n
# J(3^n + 1) = 1
# J(2*3^n) = 3^n
# Find largest n such that 3^n < N, then count up by 1's
# until you get to 2*3^n, then count by 2's from there
div = 1
while N > div*3:
	div *= 3
if N - div < div:
	print N - div
else:
	print 2*N - 3*div # 2*(N - 2*div) + div
