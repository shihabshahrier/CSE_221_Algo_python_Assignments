def selectionSort(arr, n):
    for i in range(n-1):
        m = argmin(arr, i)
        arr[i], arr[m] = arr[m], arr[i]
    
    return arr

def argmin(arr, i):
    m = i
    for j in range(i, len(arr)):
        if arr[j] < arr[m]:
            m = j
    return m

if __name__ == "__main__":
    ifile = open("input02.txt", "r")
    n, m = map(int, ifile.readline().split())
    arr = list(map(int, ifile.readline().split()))
    s = selectionSort(arr, n) 
    #print(s)
    ofile = open("output02.txt", "w")
    tx = ""
    for i in s[:m]:
        tx += str(i) + " "
    ofile.write(tx)
    ofile.close()
    ifile.close()
    