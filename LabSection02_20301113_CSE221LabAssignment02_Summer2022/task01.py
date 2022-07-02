def bubbleSort(arr, l):
    for i in range(l-1):
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    ifile = open("input01.txt", "r")
    l = int(ifile.readline())
    arr = list(map(int, ifile.readline().split()))
    b = bubbleSort(arr, l) 
    #print(b)
    ofile = open("output01.txt", "w")
    tx = ""
    for i in b:
        tx += str(i) + " "
    ofile.write(tx)
    ofile.close()
    ifile.close()
        