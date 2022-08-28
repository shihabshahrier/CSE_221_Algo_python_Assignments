import heapq

def Dijkstra(graph, start, finish):
    dist = {}
    prev = {}
    for v in graph:
        dist[v] = float('inf')
        prev[v] = None
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (dist[start], start))
    while pq:
        u = heapq.heappop(pq)[1]
        if dist[u] == float('inf'):
            break
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def solve(graph, start, finish):
    dist, prev = Dijkstra(graph, start, finish)
    path = [finish]
    while finish != start:
        finish = prev[finish]
        path.append(finish)
    path.reverse()
    return path

if __name__ == "__main__":
    ifile = open("input04.txt", "r")
    ofile = open("output04.txt", "w")
    graph = {}
    for line in ifile:
        source, destination, weight = line.split()
        if source not in graph:
            graph[source] = {}
        if destination not in graph:
            graph[destination] = {}
        graph[source][destination] = int(weight)
        graph[destination][source] = int(weight)
    #print(graph)
    solution = solve(graph, "Motijheel", "MOGHBAZAR")
    #print(solution)
    ofile.write(" ".join(map(str, solution)) + "\n")
    ifile.close()
    ofile.close()

 
# BFS is used to find the shortest path in terms of edges.
# therefore, It works well for unweighted graphs or graphs with equal weights.
# hence, The problem is related to with triffic/ weighed graphs  
# Bfs won't work for graphs with unequal weights.
# thats the reason why we use Dijkstra's algorithm.




