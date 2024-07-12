INF = int(1e9)

n = int(input())
m = int(input())

# Initialize graph
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# self to self
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# Initialize edge value
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c # costs 'c' to go from 'a' to 'b'

# Perform floyd warshall
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# Confirm 
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
