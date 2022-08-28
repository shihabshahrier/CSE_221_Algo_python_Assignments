import sys
from queue import PriorityQueue

def network(graph, source):
    dist = [-1] * len(graph)
    dist[source - 1] = 0
    Q = PriorityQueue()
    visited = [False] * len(graph)
    prev = [None] * len(graph)
    Q.put((dist[source - 1], source))
    while Q.empty() is False:
        u = Q.get()[1]
        if visited[u - 1]:
            continue
        visited[u - 1] = True
        if graph[u] is not None:
            for x in graph[u]:
                v = x[0]
                if dist[u] > x[1]:
                    alt = x[1]
                else:
                    alt = dist[u - 1] + x[1]
                if alt > dist[v - 1]:
                    dist[v - 1] = alt
                    prev[v - 1] = u
                    Q.put((dist[v - 1], v))
    if len(dist) != 1:
        lst = dist[1:]
        lst.sort()
        x = lst[0]
        dist[-1] = x
    return dist

if __name__ == "__main__":
    ifile = open("input05.txt", "r")
    ofile = open("output05.txt", "w")
    data = ifile.read()
    lines = data.split("\n")
    t = int(lines[0])
    ind = 1
    for i in range(t):
        k = lines[ind].split()
        n, m = int(k[0]), int(k[1])
        lst = []
        graph = {}
        for j in range(1, m + 1):
            lst.append(lines[ind + j])
        for x in range(len(lst)):
            lst2 = lst[x].split()
            u, v, w = int(lst2[0]), int(lst2[1]), int(lst2[2])
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
        source = int(lines[ind + m + 1])
        ind = ind + m + 2
        if graph == {}:
            ofile.write("0" + "\n")
        else:
            x = network(graph, source)
            for i in range(len(x)):
                if i == len(x) - 1:
                    ofile.write(str(x[i]) + "\n")
                else:
                    ofile.write(str(x[i]) + " ")
    ifile.close()
    ofile.close()
    sys.exit(0)

        
