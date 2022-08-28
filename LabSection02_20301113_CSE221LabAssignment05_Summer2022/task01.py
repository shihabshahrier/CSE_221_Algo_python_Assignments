ifile = open("input1.txt", "r")
t_case = int(ifile.readline())

lst = []
for i in range(t_case):
    lst.append(tuple(map(int, ifile.readline().split())))

lst.sort(key = lambda x: x[1])

count = 1
f_lst = [lst[0]]
queue = list()
onf = lst[0][1]
for c in range(1, len(lst)):
    if lst[c][0] >= onf:
        count += 1
        f_lst.append(lst[c])
        onf = lst[c][1]

ofile = open("output1.txt", "w")
ofile.write(str(count) + "\n")
for i in range(len(f_lst)):
    ofile.write(str(f_lst[i][0]) + " " + str(f_lst[i][1]) + "\n")

ofile.close()
ifile.close()
