def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
def quickSort(arr, p, q):
    if p < q:
        k = partition(arr, p, q)
        quickSort(arr, p, k - 1)
        quickSort(arr, k + 1, q)

def findK(arr, k):
    start = 0
    end = len(arr) - 1
    while start < end:
        p = partition(arr, start, end)
        if k == p:
            return arr[p]
        elif k < p:
            end = p - 1
        else:
            start = p + 1
    return arr


if __name__ == "__main__":
    ifile = open("input05.txt", "r")
    n = int(ifile.readline())
    arr = list(map(int, ifile.readline().split()))
    quickSort(arr, 0, n-1)
    k = int(ifile.readline().split()[2])
    k_val = findK(arr, k)
    #print(arr, k)
    ofile = open("output05.txt", "w")
    s = ""
    for i in arr:
        s += str(i) + " "
    ofile.write(s)
    ofile.write(f"\nKth/ {k} no value is {k_val}")
    
    ifile.close()
    ofile.close()
