from task01 import graph_

graph = graph_()
visited = [float("inf")]*(len(graph)+1)
level = [-1]*(len(graph)+1)
parent = [None]*(len(graph)+1)
queue = []

def BFS(graph, visited, node, end):
    visited[int(node)-1]= 1
    queue.append(node)
    s = ""
    while queue:
        m = queue.pop(0)
        s += str(m) + " "
        if m == end:
            break
        for n in graph[m]:
            if visited[int(n)-1] == float("inf"):
                visited[int(n)-1] = 1
                parent[int(n)-1]= m
                level[int(n)-1] = level[int(m)]+1
                queue.append(n) 
    return s

if __name__ == "__main__":
    bfs = BFS(graph, visited, "1", "12")
    ofile = open("output02.txt", "w")
    ofile.write(bfs)
    ofile.close
    # print(level)
    # print(parent)

    v = "6"
    path = ""
    while v is not None:
        path += v
        v = parent[int(v)-1]
    print(path[::-1])


    












    #print(graph)