n, m = map(int, input().split())

minInRows = []

for i in range(n):
    row = list(map(int, input().split())) # 하나의 행 입력받기
    row.sort()
    minInRows.append(row[0])

minInRows.sort()
result = minInRows[n - 1]

print(result)







