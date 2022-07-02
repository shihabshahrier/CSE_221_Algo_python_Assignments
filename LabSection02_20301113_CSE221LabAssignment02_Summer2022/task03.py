# def insertionSort(arr, n):
#     for i in range(n-1):
#         temp = arr[i+1]
#         j = i
#         while j >= 0:
#             if arr[j] > temp:
#                 arr[j+1] = arr[j]
#             else:
#                 break
#             j  -= 1
#         arr[j+1] = temp
    
#     return arr

def insertionSort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    
    return arr
        

if __name__ == "__main__":
    ifile = open("input03.txt", "r")
    n= int(ifile.readline())
    id_arr = list(map(int, ifile.readline().split()))
    mark_arr = list(map(int, ifile.readline().split()))
    dic = dict()
    for i in range(n):
        dic[id_arr[i]] = mark_arr[i]
        
    s = insertionSort(mark_arr, n) 
    rev_s = s[::-1]
    ids = []
    for i in rev_s:
        for k, v in dic.items():
            if i == v:
                ids.append(k)
                del dic[k]
                break
    #print(s)
    #print(ids)
    #print(dic)
    ofile = open("output03.txt", "w")
    tx = ""
    for i in ids:
        tx += str(i) + " "
    ofile.write(tx)
    ofile.close()
    ifile.close()

        