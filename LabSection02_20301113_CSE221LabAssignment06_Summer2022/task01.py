def reduce0(n):
    count = 0
    while n != 0:
        m = 0
        for i in str(n):
            if m < int(i):
                m = int(i)
        n -= m
        count += 1
    return count

if __name__ == "__main__":
    ifile = open("input01.txt")
    ofile = open("output01.txt", "w")
    n = int(ifile.readline())
    c = reduce0(n)
    ofile.write(str(c))
    
    ofile.close()
    ifile.close()


