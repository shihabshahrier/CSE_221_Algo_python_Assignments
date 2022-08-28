
ifile = open("input04.txt", "r")
ofile = open("output04.txt", "w")
test = int(ifile.readline())

lst = []
for i in range(test):
    graph = dict()
    n, m = list(map(int, ifile.readline().split()))
    for i in range(m):
        x, y = list(map(int, ifile.readline().split()))
        graph[x] = graph.get(x, []) + [y]
        graph[y] = graph.get(y, []) + [x]
        
    visited = [0] * n
    queue = []
    d = [0] * n
    
    def BFS(visited, graph, node):
        visited[node - 1] = 1
        queue.append(node)
        while queue:
            m = queue.pop(0)
            for i in graph[m]:
                if visited[i - 1] == 0:
                    visited[i - 1] = 1
                    queue.append(i)
                    d[i-1] = d[m-1] + 1

    BFS(visited, graph, 1)
    ofile.write(f"{d[n-1]} \n")

ofile.close()
ifile.close()
