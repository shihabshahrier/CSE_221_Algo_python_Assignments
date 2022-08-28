def graph_():
    ifile = open("input01.txt", "r")
    places = int(ifile.readline())
    connections = int(ifile.readline())
    graph = {}
    for i in range(connections):
        a, b = map(str, ifile.readline().split())
        if a not in graph:
            graph[a]=[]
        if b not in graph:
            graph[b]=[]
        graph[a].append(b)
    ifile.close()
    return graph

graph = graph_()
print(graph)
ofile = open("output01.txt", "w")
ofile.write(str(len(graph))+"\n")

for k, v in graph.items():
    s = f"{k} "
    for i in v:
        s += str(i) + " "
    print(s)
    ofile.write(s+"\n")


ofile.close()

