import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # n: 도시의 개수, m: 통로의 개수, c: 전보 시작 도시

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 그래프 생성
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # x에서 y가는데 z비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]: # i: (노드, 거리)
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
