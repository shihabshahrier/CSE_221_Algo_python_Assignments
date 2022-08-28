from task01 import graph_
graph = graph_()
visited = [float("inf")]*(len(graph)+1)
printed = []

def dfsVisit(graph, node):
    visited[int(node)] = 1
    printed.append(node)
    for i in graph[node]:
        if visited[int(i)] == float("inf"):
            dfsVisit(graph, i)

def DFS(graph, end):
    for k in graph.keys():
        if k == end:
            dfsVisit(graph, k)
            break
        if visited[int(k)-1] == float("inf"):
            dfsVisit(graph, k)
        return " ".join(map(str, printed[:printed.index(end)+1]))

if __name__ == "__main__":
    dfs = DFS(graph, "12")
    ofile = open("output03.txt", "w")
    ofile.write(dfs)
    ofile.close()
