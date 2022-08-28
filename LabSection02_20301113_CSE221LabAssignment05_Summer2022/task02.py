def schedule(requests, m):
    requests.sort(key=lambda x: x[0])
    resources = [0] * m
    count = 0
    for i in range(len(requests)):
        if resources[0] < requests[i][0]:
            resources[0] = requests[i][1]
            count += 1
        else:
            for j in range(1, m):
                if resources[j] < requests[i][0]:
                    resources[j] = requests[i][1]
                    count += 1
                    break
    return count

if __name__ == "__main__":
    ifile = open("input2.txt", "r")
    ofile = open("output2.txt", "w")
    n, m = map(int, ifile.readline().split())
    requests = []
    for line in ifile:
        requests.append(tuple(map(int, line.split())))
    print(schedule(requests, m), file=ofile)

    ifile.close()
    ofile.close()