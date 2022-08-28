def LCS(x, y, zone):
    lcs = ""
    m, n = len(x), len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    i = m
    j = n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            lcs = zone[x[i-1]] + " " + lcs
            i -= 1
            j -= 1
        elif c[i-1][j] > c[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return lcs

if __name__ == "__main__":
    zone = [["Yasnaya","Y"],["Rozhok","R"],["School","S"],
            ["Pochinki","P"],["Farm","F"],["Mylta","M"],
            ["Shelter","H"],["Prison","I"]]
    zone = dict(map(reversed, zone))
    ifile = open("input02.txt")
    ofile = open("output02.txt", "w")

    n = int(ifile.readline())
    x = list(map(str, (ifile.readline().split())))[0]
    y = list(map(str, (ifile.readline().split())))[0]
    #print(x)

    lcs = LCS(x, y, zone)
    ofile.write(lcs)
    correctness = (len(lcs.split())*100)//n
    ofile.write(f"\nCorrectness of prediction: {correctness}%")
    #print(lcs)

    ofile.close()
    ifile.close()