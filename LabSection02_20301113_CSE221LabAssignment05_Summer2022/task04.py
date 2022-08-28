ifile = open('input4.txt', 'r')
i_data = ifile.read().split("\n")

f_lst = list()
for i in i_data:
    if i != "":
        s, e = list(map(int, i.split()))
        if s == 0 and e == 0:
            break
        j = s ** .5
        count = 0
        while j * j <= e:
            count += 1
            j += 1
        f_lst.append(count)

ofile = open('output4.txt', 'w')
for i in f_lst:
    ofile.write(str(i) + "\n")

ifile.close()
ofile.close()