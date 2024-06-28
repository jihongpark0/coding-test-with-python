n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA = sorted(arrayA)
arrayB = sorted(arrayB, reverse=True)

for i in range(k):
    if arrayA[i] < arrayB[i]: # 이 조건 꼭 넣어줘야 함
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else: # 위의 경우가 아니면, 스왑을 진행할 필요가 없으므로 반복문 강제 종료
        break

print(sum(arrayA))