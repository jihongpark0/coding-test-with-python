INF = int(1e9)

n, m = map(int, input().split()) # n: 전체 회사 개수, m: 경로 개수

# 그래프 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자신에서 자신으로
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜
for s in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][s] + graph[s][b])
            
result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

