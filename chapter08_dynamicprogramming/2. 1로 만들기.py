x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    temp = []
    temp.append(d[i - 1])

    if i % 2 == 0:
        temp.append(d[i // 2])
    if i % 3 == 0:
        temp.append(d[i // 3])
    if i % 5 == 0:
        temp.append(d[i // 5])

    d[i] = min(temp) + 1

# 확인용
# for i in range(x + 1):
#     print(d[i], end=" ")

print(f"\n {d[x]}")