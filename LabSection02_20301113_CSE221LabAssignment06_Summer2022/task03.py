def lcsXthree(x, y, z):
	m, n, o = len(x), len(y), len(z)
	c = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			for k in range(o+1):
				if (i == 0 or j == 0 or k == 0):
					c[i][j][k] = 0	
				elif (x[i-1] == y[j-1] and
					x[i-1] == z[k-1]):
					c[i][j][k] = c[i-1][j-1][k-1] + 1
				else:
					c[i][j][k] = max(max(c[i-1][j][k], c[i][j-1][k]),c[i][j][k-1])
	return c[m][n][o]

if __name__ == "__main__":
    ifile = open("input03.txt")
    ofile = open("output03.txt", "w")
    x = list(map(str,ifile.readline().split()))[0]
    y = list(map(str,ifile.readline().split()))[0]
    z = list(map(str,ifile.readline().split()))[0]
    l = lcsXthree(x, y, z)

    ofile.write(str(l))

    ofile.close()
    ifile.close()
			
