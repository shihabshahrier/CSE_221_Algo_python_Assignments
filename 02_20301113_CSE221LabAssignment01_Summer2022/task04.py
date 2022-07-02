def multipyMatrix(A, B, n):
    c = [[0]*n for _ in range(n)]
    #print(c)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k]*B[k][j]
    return c

if __name__ == "__main__":  
    ifile = open("input04.txt", "r")
    n = int(ifile.readline())
    A = []
    B = []
    for i in range(2):
        for j in range(n):
            x = list(map(int, ifile.readline().split()))
            if i == 0:
                A.append(x)
            else:
                B.append(x)

    x = multipyMatrix(A, B, n)
    ofile = open("output04.txt", "w")
    for i in range(n):
        d = f"{x[i]}\n"
        ofile.write(d)
    ifile.close()
    ofile.close()
    print(x)

    