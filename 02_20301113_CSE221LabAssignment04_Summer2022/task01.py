import heapq

def dijkstra(graph, source):
    dist = {}
    prev = {}
    for v in graph:
        dist[v] = float('inf')
        prev[v] = None
    dist[source] = 0
    pq = []
    heapq.heappush(pq, (dist[source], source))
    print(pq)
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

if __name__ == "__main__":

    ifile = open("input01.txt", "r")
    ofile = open("output01.txt", "w")
    t = int(ifile.readline())
    for i in range(t):
        n, m = map(int, ifile.readline().split())
        graph = {}
        for j in range(n):
            graph[j+1] = {}
        for j in range(m):
            u, v, w = map(int, ifile.readline().split())
            graph[u][v] = w
        print(graph)
        dist, prev = dijkstra(graph, 1)
        ofile.write(str(dist[n]) + "\n")
    ifile.close()
    ofile.close()

