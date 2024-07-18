# 위상정렬을 사용하여 푸는 것이 시간복잡도 측면에서 더 우수하다.

n = int(input()) # n: 듣고자하는 강의의 수

sl = [[] for _ in range(n + 1)] # 선수과목 리스트
result = [0] * (n + 1)

for i in range(1, n + 1): # 1 ~ n
    inputList = list(map(int, input().split()))
    result[i] += inputList[0]
    for j in range(1, len(inputList) - 1):
        sl[i].append(inputList[j])

for i in range(1, n + 1):
    if len(sl[i]) == 0:
        continue

    temp = []
    for j in sl[i]:
        temp.append(result[j])

    result[i] += max(temp)

for i in range(1, n + 1):
    print(result[i])
        
    