class Node:
    num = None
    pos = None
    data = None
    linked = []
    visited = False

def dfs(graph, startNodeNum):
    graph[startNodeNum].visited = True
    print(graph[startNodeNum].num, end=' ')
    for i in graph[startNodeNum].linked: # i: 인접 노드 번호
        if graph[i].visited == False and graph[i].data == 0:
            dfs(graph, graph[i].num)


n, m = map(int, input().split())

field = [] # n행 m열의 리스트
for i in range(n):
    field.append(list(map(int, input().split())))

# 그래프 만들기
graph = [0] # 그래프 번호(1~9)랑 graph 리스트랑 맞추려고 임시로 해놓은거
nodeNum = 1
for i in range(n):
    for j in range(m):
        node = Node()
        node.num = nodeNum
        node.pos = (j, i)
        node.data = field[i][j]

        l = []
        for p in [(j-1, i), (j, i-1), (j+1, i), (j, i+1)]:
            if (p[0] >= 0 and p[0] < m) and (p[1] >= 0 and p[1] < n):
                nn = p[0] + m * p[1] + 1
                l.append(nn)

        node.linked = l

        graph.append(node)
        nodeNum += 1

iceCount = 0
for n in graph:
    if n == 0: # 그래프 번호(1~9)랑 graph 리스트랑 맞추려고 임시로 해놓은거
        continue
    if n.visited == False and n.data == 0:
        iceCount += 1
        dfs(graph, n.num)

print(f"\n\niceCount: {iceCount}")












