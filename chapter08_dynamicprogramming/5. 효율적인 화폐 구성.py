n, m = map(int, input().split()) # n: 화폐의 종류 수, m: 만들고자 하는 금액

array = [] # n종류 화폐 각각의 가치
for i in range(n):
    array.append(int(input()))

d = [0] * (m + 1)

for i in range(1, m + 1):
    temp = []
    for j in array:
        if i - j < 0:
            continue
        if d[i - j] != -1:
            temp.append(1 + d[i - j])

    if len(temp) == 0:
        d[i] = -1
        continue

    d[i] = min(temp)

print(d[m])



