n, m = map(int, input().split()) # n: 볼링공 갯수, m: 볼링공 최대 무게
data = list(map(int, input().split())) # 볼링공 무게 리스트

array = [0] * 11

for d in data:
    array[d] += 1

result = 0
for i in range(1, m + 1):
    result += array[i] * sum(array[i+1:])

print(result)