n, m = map(int, input().split()) # n: 집의 개수, m: 길의 개수

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

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

for i in range(m):
    a, b, c = map(int, input().split()) # a와 b를 연결된 길을 유지하는데 c의 비용이 든다
    edges.append((c, a, b))

edges.sort()

last = 0

# 하나의 최소신장트리 생성
for edge in edges:
    c, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += c
        last = c
    
"""
<주의>
처음에는 위의 반복문 안에서 last를 구하지 않고 edges의 마지막 edge의 비용으로 구했다. (아래)
last = edges[m - 1][0]

하지만 위는 치명적인 실수이다. edges의 마지막 요소가 가장 높은 비용의 간선인 것은 맞지만 그 마지막 요소가
MST에 포함될 보장이 없기 때문이다. 

따라서 반드시 위의 반복문 내의 조건문(MST를 실제로 형성하는) 내에 last를 구하는 과정을 포함시켜야 한다.
"""

result -= last
print(result)
