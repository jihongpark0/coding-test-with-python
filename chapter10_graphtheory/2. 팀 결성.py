n, m = map(int, input().split()) # n: 초기 n+1개의 팀, m: 연산의 총 개수

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

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

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 합치기 연산
        unionParent(parent, a, b)
    else: # 같은 팀 여부 확인 연산
        a = findParent(parent, a)
        b = findParent(parent, b)
        if a == b:
            print('YES')
        else:
            print('NO')
