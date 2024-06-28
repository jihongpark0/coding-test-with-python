n, m = map(int, input().split()) # 행 갯수, 열 갯수
x, y, dir = map(int, input().split())

def printField(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            print(field[i][j], end=' ')
        print()

# 맵 생성: 0육지, 1바다
field = []
for i in range(n):
    row = list(map(int, input().split()))
    field.append(row)

# 방문 여부 확인용 리스트: 0미방문, 1방문
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[y][x] = 1

movingDelta = {3:(-1, 0), 2:(0, 1), 1:(1, 0), 0:(0, -1)} # 좌 하 우 상 전진 이동( 방향:(dx,dy) )

moving = True
while moving:
    dirToMove = dir
    i = 0
    while i < 4: # 방향 반시계 회전
        dirToMove -= 1
        if dirToMove < 0:
            dirToMove = 3

        # 한 번 회전해서 이동할 위치 결정
        xTarget = x + movingDelta[dirToMove][0]
        yTarget = y + movingDelta[dirToMove][1]

        if field[yTarget][xTarget] == 0 and visited[yTarget][xTarget] == 0: # 육지이고 미방문이라서 이동 가능
            dir = dirToMove
            x, y = xTarget, yTarget
            visited[y][x] = 1
            print("이동")
            break

        if visited[yTarget][xTarget] == 1: # 이미 방문했음(방문했다는 것은 바다가 아니라는 것)
            dir = dirToMove
            print("좌턴")
        
        if i == 3:
            xTarget = x - movingDelta[dirToMove][0]
            yTarget = y - movingDelta[dirToMove][1]
            if field[yTarget][xTarget] == 1: # 끝
                moving = False
                print("끝: 후진 불가")
                break
            else:
                x, y = xTarget, yTarget
                visited[y][x] = 1
                i = 0
                print("후진")
                continue
        
        if field[yTarget][xTarget] == 1:
            print("좌턴")
        i += 1

count = 0
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if visited[i][j] == 1:
            count += 1
        
print(count)




