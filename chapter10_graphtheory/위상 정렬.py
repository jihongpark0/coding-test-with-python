from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

# 그래프 구조
"""
[
    0번:
    1번 노드: [연결되어있는 노드들의 번호들]
    2번 노드: [연결되어있는 노드들의 번호들]
    ...
]
"""
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동
    indegree[b] += 1

def topologySort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topologySort()
