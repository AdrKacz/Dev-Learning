f = [1, 1]

n = 10
un = -1
for i in range(n):
	un += 2
	print(" ".join([str(un + 2*j) for j in range(i + 1)]))
	un += 2*i + f[0]

	# Fibonacci
	g = f[0]
	f[0] = f[1]
	f[1] = g + f[0]