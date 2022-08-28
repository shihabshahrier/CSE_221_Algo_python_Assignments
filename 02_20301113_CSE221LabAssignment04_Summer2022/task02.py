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
def solve(graph, source, n):
    dist, prev = dijkstra(graph, source)
    path = [n]
    while n != source:
        n = prev[n]
        path.append(n)
    path.reverse()
    return path

if __name__ == "__main__":
    ifile = open("input01.txt", "r")
    ofile = open("output02.txt", "w")
    t = int(ifile.readline())
    for i in range(t):
        n, m = map(int, ifile.readline().split())
        graph = {}
        for j in range(n):
            graph[j+1] = {}
        for j in range(m):
            u, v, w = map(int, ifile.readline().split())
            graph[u][v] = w
        path = solve(graph, 1, n)
        ofile.write(" ".join(map(str, path)) + "\n")
    ifile.close()
    ofile.close()