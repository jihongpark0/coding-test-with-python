# Dijkstra algorithm using heap

# heap: (distance, nodeNumber), graph: (target, distance)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n: number of nodes(vertex), m: number of edges
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split()) # It costs 'c' to go from 'a' to 'b'
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]: # i: (target, disdtance)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])