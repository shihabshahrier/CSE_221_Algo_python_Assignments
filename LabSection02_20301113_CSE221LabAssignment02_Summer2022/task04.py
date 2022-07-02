def marge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    #print(p, q, r)
    L = [0 for i in range(n1+1)]
    R = [0 for i in range(n2+1)]
    
    for i in range(n1):
        L[i] = arr[p+i]
        
    for j in range(n2):
        R[j] = arr[q+j+1]
        
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j+= 1


    
def margeSort(arr, p, r):
    if p < r:
        q = (p+r)//2
        margeSort(arr, p, q)
        margeSort(arr, q+1, r)
        marge(arr, p, q, r)
        
        
if __name__ == "__main__":
    ifile = open("input04.txt", "r")
    n = int(ifile.readline())
    arr = list(map(int, ifile.readline().split()))
    margeSort(arr, 0, len(arr)-1)
    tx = ""
    for i in arr:
        tx += str(i) + " "
    #print(tx)
    ofile = open("output04.txt", "w")
    ofile.write(tx)
    ofile.close()
    ifile.close()
    
    
    
    
    
    
    
    
    