def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split()) # node a와 node b를 연결한 간선은 cost의 비용을 가진다는 뜻
    edges.append((cost, a, b)) # cost를 기준으로 오름차순 정렬하기 위해 cost를 맨 앞에 위치시킴

edges.sort()

# 핵심적인 부분
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost

print(result)