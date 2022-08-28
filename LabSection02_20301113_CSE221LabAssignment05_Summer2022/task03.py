ifile = open("input3.txt", "r")
t = int(ifile.readline())
a_lst = list(map(int, ifile.readline().split()))
a_lst.sort()
s_lst = str(ifile.readline())

ss = list()
seq = ""
J_hour = 0
j_hour = 0
idx = 0
for c in s_lst:
    if c == "J":
        ss.append(idx)
        seq += str(a_lst[idx])
        J_hour += a_lst[idx]
        idx += 1
    elif c == "j":
        x = ss.pop()
        seq += str(a_lst[x])
        j_hour += a_lst[x]

ofile = open("output3.txt", "w")
ofile.write(seq + "\n")
ofile.write("Jack will work for " + str(J_hour)+ " hours\n")
ofile.write("Jill will work for " + str(j_hour)+ " hours\n")
ofile.close()
ifile.close()